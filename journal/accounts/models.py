from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
        Custom user class so i can add other settings later or field to do user

    '''

    # customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL,
    #                              help_text="The user's Stripe Customer object, if it exists")
    # subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL,
    #                                  help_text="The user's Stripe Subscription object, if it exists")
