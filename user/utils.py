# Bloom User component
#
# Kevin Tom
# Copyright 2008 Handi Mobility
# www.handimobility.ca

from django.db import models
from django.contrib.auth.models import User

from bloom.user.models import UserPhoneNumber


def get_or_create_user_by_phonenumber(number):
    user_number = UserPhoneNumber.objects.filter(number=number)
    if user_number.count() == 0:
        user = User.objects.create_user(number,'numberonly@localhost', 'non-valid password')
        user.is_active = False
        user.save()
        un = UserPhoneNumber(user=user,number=number,name=number)
        un.save()
        return user
    else:
        return user_number.select_related().get()
            
def get_or_create_user_by_email(email):
    user, created = User.objects.get_or_create(email=email, defaults={'username':email})
    if created == True:
        user.is_active = False
    return user