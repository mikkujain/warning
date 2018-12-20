from django.shortcuts import render

import json
import urllib.request
import urllib.parse

def sendSMS(provider, numbers, sender, message):
    data =  urllib.parse.urlencode(
        {
            'apikey': provider.apikey,
            'numbers': numbers,
            'message' : message,
            'sender': sender
        }
    )
    data = data.encode('utf-8')

    request = urllib.request.Request(provider.send_url)
    try:
        f = urllib.request.urlopen(request, data, timeout=20)
    except urllib.request.URLError as e:
        raise Exception('Failed to send SMS: ' + str(e))

    fr = f.read()
    fr = json.loads(fr.decode('utf-8'))
    if fr.get('status') == 'failure':
        e = 'sendSMS(): ' + ', '.join([x.get('message') for x in fr.get('errors')])
        raise Exception(e)

    return(fr)
