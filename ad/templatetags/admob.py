# Bloom Framework
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.template import Library, Node

from bloom.utils import get_setting
from bloom.ad.utils import get_admob		 

register = Library()


"""
{% load admob %}

{% admob %}

"""

class AdmobNode(Node):
		def render(self, context):
#			print context
			return get_admob(context['request'])

def admob(parser, token):
	"""
	Generate a simple admob ad with
	no targetting.
	"""
	return AdmobNode()
register.tag(admob)
