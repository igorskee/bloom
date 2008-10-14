# Models for Bloom SMS component to record sent and received sms messages
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.db import models
from django.contrib import admin

class SentSMS(models.Model):
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    success = models.BooleanField()
    fullresponse = models.TextField()
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s -> %s" % (self.phone_number, self.message)

    class Admin:
        pass

class ReceivedSMS(models.Model):
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    carrier = models.CharField(max_length=10)
    provider_number = models.CharField(max_length=20)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s -> %s" % (self.phone_number, self.message)    
    
    class Admin:
        pass
        
admin.site.register(SentSMS)
admin.site.register(ReceivedSMS)