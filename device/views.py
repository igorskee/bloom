# Bloom Framework
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.shortcuts import render_to_response
from django.template import RequestContext

from bloom.device.decorators import detect_device

@detect_device
def detect_device_test(request):
	"""
	Device information is now availible in request.device 
	"""
	return render_to_response('test.html', context_instance=RequestContext(request))



'''
	"""
	We coudl put some of this other shit in there:
	"""

#	print request.META

	ua = request.META['HTTP_USER_AGENT']
	apiRevision = da.getApiRevision()

    
	recogStart = time.time()
	props = da.getPropertiesAsTyped(tree, ua)
	recogEnd = time.time()

	if props.has_key('vendor') and props.has_key('model'):
		imgSrc = 'http://deviceatlas.com/sites/deviceatlas.com/themes/eris/img/device_images/%s/%s.jpg' % (props['vendor'].lower(), props['model'].lower())
	else:
		imgSrc = False

	context_dict = {
		'apiRevision': apiRevision,
		'props': props,
		'imgSrc': imgSrc,
		'ua': ua,
		't': True,
		'f': False,
		'loadTime': loadEnd - loadStart,
		'recogTime': recogEnd - recogStart,
		'recogPerSec': int(1/(recogEnd - recogStart)),
		'server_name': request.META['SERVER_NAME'],
	}

	mobileDevice = False
	if props.has_key('mobileDevice'):
		if props['mobileDevice']:
				mobileDevice = True

		if mobileDevice:
			return render_to_response('index.xhtml', context_dict)
	
	return render_to_response('index.html', context_dict)
'''	
		