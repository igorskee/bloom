# Bloom SMS component Upside Connector
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca


from django.conf import settings
from bloom.sms.lib.upside.Authentication_client import *
from bloom.sms.lib.upside.SMS_client import *

class UpsideConnector:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = (str(settings.BLOOM_SMS_UPSIDE_TOKEN)) or self.get_token_signature()["token"]
        self.signature = (str(settings.BLOOM_SMS_UPSIDE_SIG)) or self.get_token_signature()["signature"]
        self.sms_soap = SMSSoapSOAP( SMSLocator.SMSSoap_address )

    def send_plain_sms(self, msg, recipient):
        #for rcpt in receipient_list:
		#    sms_result = self.sms_soap.Send_Plain( \
		#	    token=self.token, \
        #        signature=self.signature, \
		#		recipient= rcpt, \
        #        message= msg, \
        #        encoding='Seven' )
        sms_result = self.sms_soap.Send_Plain(token=self.token,
                                              signature=self.signature,
                                              recipient=recipient,
                                              message=msg,
                                              encoding='Seven')
        return sms_result

			
    def verify_connect(self):
        sms_result = self.sms_soap.Send_Test(token=self.token, 
											 signature=self.signature,
											 recipient= '16045555555',
											 message= 'Test_Validation_Only',
											 encoding= 'Seven' )
        return sms_result

    def get_token_signature(self):
        credentials = {}
        auth_soap = AuthenticationSoapSOAP( AuthenticationLocator.AuthenticationSoap_address )
        auth_result = auth_soap.GetParameters( self.username, self.password)
        credentials["token"] = auth_result.Token
        credentials["signature"] = auth_result.Signature
        return credentials
        
    def was_send_successful(self, sms_result):
        if ((sms_result.isOk == True) and (sms_result.tooManyMessages == False) and (sms_result.isBlocked == False)):
            return True
        else:
            return False
    
    def get_fullresponse(self, sms_result):
        fullresponse = "isOk=%s trackingId=%s number=%s convertedNumber=%s deferUntilOccursInThePast=%s messageIsEmpty=%s tooManyMessages=%s invalidCountryCode=%s isBlocked=%s BlockedReason=%s" % (
                                sms_result.isOk,
                                sms_result.trackingId,
                                sms_result.number,
                                sms_result.convertedNumber,
                                sms_result.deferUntilOccursInThePast,
                                sms_result.messageIsEmpty,
                                sms_result.tooManyMessages,
                                sms_result.invalidCountryCode,
                                sms_result.isBlocked,
                                sms_result.BlockedReason
                                )
        return fullresponse

        
def upside_receive_sms(self, request):
    receive = {}
    receive["username"] = request.POST.get('name', '')
    receive["sender"] = request.POST.get('sender', '')
    receive["message"] = request.POST.get('data', '')
    receive["carriercode"] = request.POST.get('carriercode', '')
    receive["inboundnumber"] = request.POST.get('inboundnumber', '')
    return receive