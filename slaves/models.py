from django.db import models

class System(models.Model):
    name = models.CharField(max_length=100)
    number_slaves = models.IntegerField()

    def __str__(self):
        return self.name

class Slave(models.Model):
    name = models.CharField(max_length=100, default='')
    sid = models.IntegerField()
    ip = models.GenericIPAddressField(protocol='IPv4')
    port = models.IntegerField()
    query_frequency = models.IntegerField()
    system = models.ForeignKey('System', on_delete=models.CASCADE)
    primary = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    address = models.IntegerField()
    nregisters = models.IntegerField()
    slave = models.ForeignKey('Slave', on_delete=models.CASCADE)
    isFlags = models.BooleanField(default=False)
    multiplication_factor = models.FloatField(default=1)
    img = models.ImageField(null=True, blank=True, upload_to='media')
    has_icon = models.BooleanField(default=False)
    icon = models.CharField(null=True,blank=True,max_length=250)


    def __str__(self):
        return self.name
        
    def getIcon(self):
        return self.has_icon


class Flag(models.Model):
    name = models.CharField(max_length=100)
    bit_location = models.IntegerField()
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE) # XXX:only isFlags==True?
    send_alert = models.BooleanField(default=False)
    img = models.ImageField(null=True, blank=True, upload_to='media')
    has_icon = models.BooleanField(default=False)
    icon = models.CharField(null=True,blank=True,max_length=250)


    def __str__(self):
        return self.name

    def getIcon(self):
        if self.has_icon:
            return self.icon
        elif self.img:
            return self.img.url

class Threshold(models.Model):
    threshold = models.FloatField()
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    address = models.IntegerField()

    def __str__(self):
        return self.sensor.name

class Log(models.Model):
    timestamp = models.DateTimeField()
    slave_id = models.IntegerField()
    eventid = models.IntegerField()
    event_name = models.CharField(max_length=100)
    event_msg = models.TextField()
    value = models.FloatField()

class Alert(models.Model):
    name = models.CharField(max_length=20)

    SMS = 'SMS'
    EMAIL = 'Email'
    ALERT_LIST = (
        (SMS, 'SMS'),
        (EMAIL, 'Email'),
    )
    alert_type = models.CharField(max_length=5,
                                  choices=ALERT_LIST,
                                  default=EMAIL)
    enabled = models.BooleanField(default=False)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=1000)
    default_expiry_time = models.IntegerField('Time to wait for next alert in minutes')
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
