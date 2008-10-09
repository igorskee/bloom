# Bloom Track component
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.db import models
from django.contrib.auth.models import User

from bloom.track.managers import TrackManager

class Track(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, db_index=True)

	# Since session records are deleted when the user logs out we need to keep more
	# specific information about what the user is doing
	# session = models.ForeignKey(Session, db_index=True, null=True, blank=True)
	# Django sessions are 40 characters in length.
	## Is this field going to be unique over time?
	## There may come a time when a session key is reused...
	session_key = models.CharField(max_length=40, null=True, blank=True)

	requested_url = models.CharField(max_length=254, db_index=True)
	requested_view_name = models.CharField(max_length=64, null=True, blank=True)

	referer_url = models.URLField(verify_exists=False, db_index=True, blank=True, null=True)
	
	client_ip = models.IPAddressField(blank=True,null=True)
	client_host = models.CharField(max_length=254,blank=True,null=True)
	client_ua = models.CharField(max_length=254, null=True,blank=True)
	client_device = models.CharField(max_length=64, null=True, blank=True)
	
	ctime = models.DateTimeField(auto_now_add=True, db_index=True)
	
	objects = TrackManager()
	
	def __unicode__(self):
		if self.user is None:
			return self.requested_url
		else:
			return "%s (%s)" % (self.requested_url, self.user,)