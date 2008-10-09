# Bloom Framework
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca
from bloom.device.utils import get_device

class DeviceDetectMiddleware(object):
	def process_request(self, request):
		"DeviceMiddleware adds device information to every request."
		request.device = get_device(request)