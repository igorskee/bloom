# Utils for Bloom Share component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

import random, string

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string

from bloom.sms import send_sms
from bloom.utils import get_setting
from bloom.share.models import SharedLink
from bloom.user.utils import get_or_create_user_by_phonenumber, get_or_create_user_by_email

SHARE_BASE_URL = get_setting('SHARE_BASE_URL')
SHARE_SLUG_LENGTH = get_setting('SHARE_SLUG_LENGTH', override=5)

VALID_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
def lookup_url(request, slug):
	"Returns the URL belonging to this slug if it exists"
	queryresults = get_object_or_404(SharedLink, generated_slug=slug)
	return queryresults.original_url


def share_url(sharer, url, medium, sharee):
	for i in range(1,10):
		slug = generate_slug(settings.BLOOM_SHARE_SLUG_LENGTH)
		share_dict = {'sharer':sharer, 'original_url':url, 'medium':medium, 'sharee':sharee}        
		slink, created = SharedLink.objects.get_or_create(generated_slug=slug, defaults=share_dict)
		if created:
			break
	else:
		slug = generate_slug(SHARE_SLUG_LENGTH + 1)
		slink = SharedLink.objects.create(sharer=sharer, original_url=url, generated_slug=slug, medium=medium, sharee=sharee)
	
	return slink.get_shared_url()
    
    
def share_by_email(request, url, email, subject_template='emailsubject.txt', body_template='emailbody.txt'):

	# from django.template.loader import render_to_string
	# rendered = render_to_string('my_template.html', { 'foo': 'bar' })
	# http://www.djangoproject.com/documentation/templates_python/

	sharer = request.user
	medium = 'email'
	sharee = get_or_create_user_by_email(email)
	link = share_url(sharer, url, medium, sharee)
	
	extra_context = {'sharer': sharer, 'sharelink': link, 'email': email}

	subject = render_to_string(subject_template, extra_context)
	body = render_to_string(body_template, extra_context)

	return send_mail(subject, body, sharer.email, [email], fail_silently=True)
    
def share_by_sms(request, url, phone_number, body_template='smsbody.txt'):
	sharer = request.user
	medium = 'sms'
	sharee = get_or_create_user_by_phonenumber(phone_number)
	link = share_url(sharer, url, medium, sharee)

	extra_context = {'sharer': sharer, 'sharelink': link}
	message = render_to_string(body_template, extra_context)

	return send_sms(message, [phone_number])
    
def generate_slug(length=4):
	"Generates a random string of length"
	return ''.join([random.choice(VALID_CHARS) for i in range(length)])