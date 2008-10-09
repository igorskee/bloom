# Bloom Framework
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca
from bloom.device.utils import get_device

def detect_device(view):
	"Modifies the `request` adding device information in `request.device`"
	def _decorator(request, *args, **kwargs):
	
		if not hasattr(request, "device"):
			request.device = get_device(request)
	
		return view(request, *args, **kwargs)
	
	_decorator.__doc__ = detect_device.__doc__
	_decorator.__name__ = detect_device.__name__
	
	return _decorator