# Bloom Framework
#
# John Boxall
# Copyright 2008 Handi Mobility
# www.handimobility.ca

import re
import math

from django.template import Library, TemplateSyntaxError

try:
	from sorl.thumbnail.main import get_thumbnail_setting
	from sorl.thumbnail.processors import dynamic_import, get_valid_options
	from sorl.thumbnail.templatetags.thumbnail import quality_pat, PROCESSORS, VALID_OPTIONS, ThumbnailNode
except Exception, e:
	raise Exception, "Hey you forgot to install sorl-thumbnail - its needed for this"

register = Library()

BORDER = 10


class DeviceImageNode(ThumbnailNode):
	def render(self, context):
		# Set the size of the image to fit the device.
		if hasattr(context['request'], 'device') and \
			 context['request'].device.has_key('displayWidth') and \
			 context['request'].device.has_key('displayHeight'):
			width = context['request'].device['displayWidth'] - BORDER
			height = context['request'].device['displayHeight']	
			self.requested_size = (int(width), int(height))
			
			print 'Requested Size: ' + str(self.requested_size)
			
		return super(DeviceImageNode, self).render(context)


def device_image(parser, token):
		"""
		{% device_image path_to_image %}
		
		To have a default size:
		
		{% device_image path_to_image 75x75 %}
		
		To do more
		
		{% device_image path_to_image 75x75 as image %}
		{{ image.width }} x {{ image.height }}	
		"""
		args = token.split_contents()
		tag = args[0]
		# Check to see if we're setting to a context variable.
		if len(args) in (5, 6) and args[-2] == 'as':
				context_name = args[-1]
				args = args[:-2]
		else:
				context_name = None

		if len(args) not in (3, 4):
				raise TemplateSyntaxError("Invalid syntax. Expected "
						"'{%% %s source size [options] %%}' or "
						"'{%% %s source size [options] as variable %%}'" % (tag, tag))

		# Get the source image path and requested size.
		source_var = args[1]
		size_var = args[2]

		# Get the options.
		if len(args) == 4:
				args_list = args[3].split(',')
		else:
				args_list = []

		# Check the options.
		opts = []
		kwargs = {} # key,values here override settings and defaults

		for arg in args_list:
				if arg in VALID_OPTIONS:
						opts.append(arg)
				else:
						m = quality_pat.match(arg)
						if not m:
								raise TemplateSyntaxError(
					"'%s' tag received a bad argument: '%s'" % (tag, arg))
						kwargs['quality'] = int(m.group(1))
		return DeviceImageNode(source_var, size_var, opts=opts,
							 context_name=context_name, **kwargs)
							 
register.tag(device_image)