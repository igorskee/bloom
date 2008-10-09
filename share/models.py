# Models for Bloom Share component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from bloom.utils import get_setting

SHARE_BASE_URL = get_setting('SHARE_BASE_URL')

class SharedLink(models.Model):
    sharer = models.ForeignKey(User,related_name='sharedlink_set')
    original_url = models.URLField()
    generated_slug = models.CharField(max_length=40, unique=True)
    sharee = models.ForeignKey(User,related_name='receivedlink_set')
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    medium = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s -> %s" % (self.generated_slug, self.original_url,)

    def get_shared_url(self):
        return "%s/%s" % (SHARE_BASE_URL, self.generated_slug,)

    class Admin:
        pass
        

admin.site.register(SharedLink)