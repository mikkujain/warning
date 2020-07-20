from django.contrib import admin

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import *

class ThresholdAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print('save_model(): ')
        subordinate = obj.sensor.subordinate
        try:
            client = ModbusTcpClient(subordinate.ip, subordinate.port)

            if obj.sensor.multiplication_factor != 1:
                obj.threshold = int(obj.threshold / obj.sensor.multiplication_factor)
                print('obj.threshold:', obj.threshold)

            value = client.write_register(address=obj.address,
                                          value=obj.threshold,
                                          unit=subordinate.sid)
            if value.isError():
                raise Exception(value)
            else:
                super().save_model(request, obj, form, change)

        except Exception as err:
            print(err)
            raise err           # XXX: print error on admin template
        finally:
            client.close()

class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'nregisters', 'isFlags')

class FlagAdmin(admin.ModelAdmin):
    list_display = ('name', 'bit_location', 'sensor')

class LogAdmin(admin.ModelAdmin):
    list_display = ('timestamp',)

from .models import System
admin.site.register(System)

from .models import Subordinate
admin.site.register(Subordinate)

from .models import Sensor
admin.site.register(Sensor, SensorAdmin)

from .models import Flag
admin.site.register(Flag, FlagAdmin)

from .models import Threshold
admin.site.register(Threshold, ThresholdAdmin)

from .models import Alert
admin.site.register(Alert)

from .models import Log
admin.site.register(Log, LogAdmin)
