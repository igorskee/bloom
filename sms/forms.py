# Bloom SMS component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django import forms
from django.core.validators import isOnlyDigits


class SendSMSForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(), max_length=140)
    phone_number = forms.CharField()

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone Numbers can only contain numbers")
        return phone_number
