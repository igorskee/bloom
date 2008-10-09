# Share URLs for Bloom
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca
# sample change

from django.conf.urls.defaults import *

urlpatterns = patterns('bloom.share.views',

	(r'^lookup/(?P<slug>[A-Za-z0-9]+)/$', 'lookup_view'),

	# (r'^email/$', 'share_by_email_view'),
	# (r'^sms/$', 'share_by_sms_view'),

)