# Bloom Track component
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.db import models

class TrackManager(models.Manager):

	def create_from_request(self, request):
		"""
		Create a Track object from a Request.
		"""
		#291 	def resolve(path, urlconf=None):
		#292 	    return get_resolver(urlconf).resolve(path)
		# might be able to write down the name of the
		# function and the view - this would be a lot eariser
		#		print view
		#		print args
		#		print kwargs	
		#		print resolve(request.get_full_path())
		#		print request.session.

		device = None
		if hasattr(request, "device"):
			device = "%s %s" % (request.device.get("vendor"), request.device.get("model"),)
			

		return super(TrackManager, self).create(
			user = request.user,
			session_key = request.session.session_key,
			requested_url = request.get_full_path(), #request.META["PATH_INFO"],
			requested_view_name = None, # this is where we can throw in the kwargs
			referer_url = request.META.get("HTTP_REFERER"),
			client_ip = request.META.get("REMOTE_ADDR"),
			client_host = request.META.get("REMOTE_HOST"),
			client_ua = request.META.get("HTTP_USER_AGENT"),
			client_device = device)
