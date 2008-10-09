# Bloom Share component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django import forms
from django.core.validators import isOnlyDigits


class ShareByEmailForm(forms.Form):
    url = forms.URLField(initial='http://')
    email = forms.EmailField()

class ShareBySMSForm(forms.Form):
    url = forms.URLField(initial='http://')
    phone_number = forms.CharField()
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number', '')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone Numbers can only contain numbers")
        return phone_number