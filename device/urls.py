# Bloom Framework
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

"""
Add this line to your site's root URLConf::   
	
	 (r'^device/', include('bloom.device.urls')),
	 
Then navigate to::

	.../device/test/
	
To see some statistics on device detection!

"""
from django.conf.urls.defaults import *

urlpatterns = patterns('bloom.device.views',
	(r'^test/$', 'detect_device_test'),
)