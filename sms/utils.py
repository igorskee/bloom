# Bloom SMS component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca
import types

from django.conf import settings

from bloom.sms.models import SentSMS, ReceivedSMS
from bloom.utils import get_setting


SMS_PROVIDER_UPSIDE = 'UPSIDE'

SMS_SERVICE_PROVIDER = get_setting('SMS_SERVICE_PROVIDER')
	
if SMS_SERVICE_PROVIDER == SMS_PROVIDER_UPSIDE:
	from bloom.sms.lib.upside.connector import UpsideConnector
	from bloom.sms.lib.upside.connector import upside_receive_sms

SMS_SERVICE_USERNAME = get_setting('SMS_SERVICE_USERNAME')
SMS_SERVICE_PASSWORD = get_setting('SMS_SERVICE_PASSWORD')
SMS_RECORD_SENT = get_setting('SMS_RECORD_SENT', override=False)
SMS_RECORD_RECEIVED = get_setting('SMS_RECORD_RECEIVED', override=False)



class SendSMS(object):
    def __init__(self):
        if SMS_SERVICE_PROVIDER == SMS_PROVIDER_UPSIDE:
            self.connector = UpsideConnector(SMS_SERVICE_USERNAME, SMS_SERVICE_PASSWORD)
        else:
            raise Exception('SMS service provider not found. Check BLOOM_SMS_SERVICE_PROVIDER.')
		
    def send_sms(self, message, recipient_list, fail_silently=True):
        "Sends sms messages to the aggregator defined in the settings file"
        if type(recipient_list) != types.ListType:
            raise Exception('Expecting a list of recipients to send SMS.')
        
        returnlist = []
        for rcpt in recipient_list:
            response = self.connector.send_plain_sms(message, rcpt)
            successful = self.connector.was_send_successful(response)
            fullresponse = self.connector.get_fullresponse(response)
            returnlist.append(successful)
            self.__record_sent_sms(rcpt, message, successful, fullresponse)
            
        return returnlist
			
    def test_connect(self):
        response = self.connector.verify_connect()
        return self.connector.was_send_successful(response)
        
    def __record_sent_sms(self, recipient, message, success, fullresponse):
        print SMS_RECORD_SENT
        if SMS_RECORD_SENT == True:
            SentSMS.objects.create(phone_number=recipient, message=message, success=success, fullresponse=fullresponse)
            
def receive_sms(request):
    "Receives sms messages, logs them, and then returns the contents of the sms"
    if SMS_SERVICE_PROVIDER == SMS_PROVIDER_UPSIDE:
        msg = upside_receive_sms(request)
    else:
				raise Exception('SMS service provider not found. Check BLOOM_SMS_SERVICE_PROVIDER.')
    
    if SMS_RECORD_RECEIVED == True:    	
    		ReceivedSMS.objects.create(
    			phone_number=msg["sender"],
    			message=msg["message"],
    			carrier=msg["carriercode"],
    			provider_number=msg["inboundnumber"])
    			
    return msg
