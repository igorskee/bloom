# Bloom SMS component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from bloom.sms import send_sms
from bloom.sms.forms import SendSMSForm

def send_sms_view(request, template_name='send_sms_view.html', success_url='/smstest'):
    if request.method == 'POST':
        form = SendSMSForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            phone_number = form.cleaned_data['phone_number']
            sms = send_sms(message, [phone_number])
            return HttpResponseRedirect(success_url)
    else:
        form = SendSMSForm()
    return render_to_response(template_name, {'form': form})