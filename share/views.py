# Views for Bloom Share component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.defaults import page_not_found

from bloom.share.forms import ShareByEmailForm, ShareBySMSForm
from bloom.share.utils import share_by_email, share_by_sms, lookup_url

def share_by_email_view(request, template='share_by_email_view.html', success_url='/share/success/'):
    if request.method == 'POST':
        form = ShareByEmailForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            email = form.cleaned_data['email']
            share_by_email(request, url, email)
            return HttpResponseRedirect(success_url)
    else:
        form = ShareByEmailForm()        
    return render_to_response(template, {'form': form})

def share_by_sms_view(request, template='share_by_sms_view.html', success_url='/share/success/'):
    if request.method == 'POST':
        form = ShareBySMSForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            phone_number = form.cleaned_data['phone_number']
            share_by_sms(request, url, phone_number)
            return HttpResponseRedirect(success_url)
    else:
        form = ShareBySMSForm()
    return render_to_response(template, {'form': form})
    
def lookup_view(request, slug=None):
    redirect_url = lookup_url(request, slug)
    return HttpResponseRedirect(redirect_url)
        