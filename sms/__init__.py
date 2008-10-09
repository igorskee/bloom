# Bloom SMS component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from bloom.sms.utils import SendSMS

def send_sms(message, recipient_list):
    sms = SendSMS()
    return sms.send_sms(message, recipient_list)
