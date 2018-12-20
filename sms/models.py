from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    apikey = models.CharField(max_length=1024, null=True, blank=True)
    username = models.CharField(max_length=100)
    secure_hash = models.CharField(max_length=1024, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    send_url = models.URLField(max_length=200)
    test = models.BooleanField(default=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name
