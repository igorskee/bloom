# Bloom Track component
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from bloom.track.models import Track

class TrackMiddleware(object):
	def process_response(self, request, response):
		"""
		Tracking Middleware processes all requests!
		"""
		Track.objects.create_from_request(request)
		
		return response