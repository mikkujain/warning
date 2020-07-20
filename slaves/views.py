from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
import django.core.exceptions as djexcept
from django.contrib.auth.decorators import login_required

import csv
import time
import traceback
import datetime

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import *

from .models import *
import sms.models as sms
from sms.views import *

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart

@login_required(login_url='/')
def index(request):
    print('POST:', request.POST)
    if request.POST.get('flag'):
        toggle_flag(request)
        time.sleep(1)
        return redirect('index', permanent=False)

    result = refresh_values(request)
    sensor_data = {}
    for sensor in result.get('sensor_data'):
        name = sensor.get('name').split(' ')[0]
        if name not in sensor_data.keys():
            sensor_data[name] = []
        sensor_data[name].append(sensor)

    system = System.objects.get(id=1) # XXX: hard-coding
    
    data =  [
        ['DateTime', 'Water_Level'],
        [2004, 100],
        [2005, 117],
        [2006, 660],
        [2007, 103],
        [2008, 100],
        [2009, 117],
        [2010, 660],
        [2011, 103],
    ]
    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    chart = LineChart(data_source, height=300, width=1000)
    context = {
        'errors': result.get('errors'),
        'sensor_data': sensor_data,
        'system_name': system.name,
        'chart': chart,
    }
    return render(request, 'sensor_list.html', context)

def refresh_values(request):
    result = {}
    errors = []
    sensor_data = []
    thresholds = []
    subordinate = None
    client = None

    try:
        subordinate = Subordinate.objects.get(primary=True)
    except Exception as err:
        print(err)
        e = {'error': True,
             'message': str(err)}
        errors.append(e)
        result['errors'] = errors
        result['sensor_data'] = sensor_data
        return result

    try:
        client = ModbusTcpClient(subordinate.ip, subordinate.port)

        system = System.objects.get(id=1) # XXX: hard-coding

        for sensor in subordinate.sensor_set.all():
            sensor_values = client.read_holding_registers(address=sensor.address,
                                                          count=sensor.nregisters,
                                                          unit=subordinate.sid)
            if sensor_values.isError():
                raise Exception(sensor_values)

            sensor_values = sensor_values.registers

            final_value = 0
            for i in range(sensor.nregisters):
                # Most Significant Byte (MSB) first system
                # registers are 2-bytes/16-bits each
                final_value += sensor_values[i] << (16 * (sensor.nregisters - i - 1))

            if sensor.isFlags:
                # print(bin(final_value))
                for flag in sensor.flag_set.all():
                    # Don't return spare flag values
                    if 'Spare' in flag.name:
                        continue
                    # print(flag.name, (final_value >> flag.bit_location) & 0x01)
                    flag_val = (final_value >> flag.bit_location) & 0x01
                    sensor_data.append({
                        'name': flag.name,
                        'value': flag_val,
                        'getIcon': flag.getIcon(),
                        'has_icon': flag.has_icon,
                    })
                    if flag_val > 0 and flag.send_alert == True:
                        try:
                            ## Template: Sainj Warning System, gates are being opened.
                            msg = system.name + ', gates are being opened.'
                            send_alert(msg)
                        except Exception as err:
                            print(err, ': ', err.args)
                            errors.append({
                                'error': True,
                                'message': str(err)
                            })
            else:
                count = sensor.threshold_set.count()
                if count > 0:
                    addr = sensor.threshold_set.all()[0].address
                    sensor_threshold = client.read_holding_registers(
                        address=addr,
                        count=1, # XXX: only 1 register for thresholds
                        unit=subordinate.sid
                    )
                    if sensor_threshold.isError():
                        raise Exception(sensor_threshold)

                    if final_value >= sensor_threshold.registers[0]:
                        try:
                            ## Template: Sainj Warning System, sensor #Custom1# is above threshold: #Custom2#
                            msg = system.name + ', sensor ' + sensor.name + \
                                ' is above threshold: ' + \
                                str(round(final_value * sensor.multiplication_factor, 2))
                            send_alert(msg)
                        except Exception as err:
                            print(err, ': ', err.args)
                            errors.append({
                                'error': True,
                                'message': str(err)
                            })
                        thresholds.append(sensor.name)

                if sensor.multiplication_factor != 1:
                    final_value = final_value * sensor.multiplication_factor
                    if type(final_value) == float:
                        final_value = round(final_value, 3)

                # Don't return spare register values
                if 'Spare' not in sensor.name:
                    sensor_data.append({
                        'name': sensor.name,
                        'value': final_value
                    })

        sensor_data.append({'name': 'thresholds',
                            'value': thresholds
        })

        result['errors'] = errors
        result['sensor_data'] = sensor_data
        
    except Exception as err:
        print(err)
        e = {'error': True,
             'message': str(err)}
              # 'trace': err.} ## XXX: show traceback
        errors.append(e)
        result['errors'] = errors
        result['sensor_data'] = sensor_data
        return result

    finally:
        if client != None:
            client.close()

    values_string = ','.join([sensor['name']+': '+str(sensor['value']) for sensor in sensor_data])
    log = Log(timestamp=timezone.now(),
              subordinate_id=subordinate.sid,
              eventid=0,          # XXX: hard-coding
              event_name='refresh_values',
              event_msg=values_string,
              value = 0         # XXX: hard-coding
    )
    log.save()

    with open('system.log', 'at', newline='') as f: # XXX: db config
        fieldnames = ['timestamp', 'subordinate_id', 'eventid', 'event_name', 'event_msg', 'value']
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow([log.timestamp, log.subordinate_id, log.eventid,
                         log.event_name, log.event_msg, log.value])

    return result


def toggle_flag(request):
    try:
        subordinate = Subordinate.objects.get(primary=True)

    except djexcept.ObjectDoesNotExist:
        err = 'No primary subordinate found.'
        print(err)
        e = {'error': True,
             'message': err}
        result.append(e)
        return result

    except djexcept.MultipleObjectsReturned:
        err = 'Multiple primary subordinates found, please select one.'
        print(err)
        e = {'error': True,
             'message': err}
        result.append(e)
        return result


    client = None
    try:
        client = ModbusTcpClient(subordinate.ip, subordinate.port)
        obj = Flag.objects.filter(name=request.POST.get('flag')).get()
        current_value = client.read_holding_registers(address=obj.sensor.address,
                                                      count=obj.sensor.nregisters,
                                                      unit=subordinate.sid)

        current_value = current_value.registers

        if obj.sensor.nregisters == 1:
            current_value = current_value[0] # LSB        # XXX: hard-coding
            future_value = current_value ^ (1 << obj.bit_location)
            value = client.write_register(address=obj.sensor.address,
                                          value=future_value,
                                          unit=subordinate.sid)
            if value.isError():
                raise Exception(value)

    except Exception as err:
        print(err)
        e = {'error': True,
             'message': str(err)}
        return e

    finally:
        if client != None:
            client.close()

def send_alert(message):
    print(message)
    alerts = Alert.objects.filter(enabled=True)
    if len(alerts) == 0:
        raise Exception('No alerts configured')

    for alert in alerts:
        print('alert.expires_at:', alert.expires_at)
        if alert.expires_at != None and timezone.now() < alert.expires_at:
            print(alert.name + ': alert not expired yet')
            return

        print(alert.receiver)
        print(alert.name + ': sending alert')
        if alert.alert_type == 'SMS':
            provider = sms.Provider.objects.get(default=True)
            sendSMS(provider=provider,
                    numbers=alert.receiver,
                    sender=alert.sender,
                    message=message)
            alert.expires_at = timezone.now() + \
                datetime.timedelta(minutes=alert.default_expiry_time)
            alert.save(update_fields=['expires_at'])

        if alert.alert_type == 'Email':
            pass                # XXX

