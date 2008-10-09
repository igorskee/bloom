# Bloom User component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserPhoneNumber(models.Model):
    # This is the only required field
    user = models.ForeignKey(User)

    # The rest is completely up to you...
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s -> %s" % (self.user.username, self.number,)
        
    class Admin:
        pass
        
admin.site.register(UserPhoneNumber)