# Bloom Track component
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.conf import settings
from django.core.urlresolvers import resolve

from bloom.track.models import Track

def track(view):
	"""
	Decorator saves the fact we hit this view.
	"""
	def _decorator(request, *args, **kwargs):	

		Track.objects.create_from_request(request)
		
		return view(request, *args, **kwargs)
		
	_decorator.__doc__ = track.__doc__
	_decorator.__name__ = track.__name__

	return _decorator