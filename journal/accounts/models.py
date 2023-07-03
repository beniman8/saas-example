from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class AccountManager(models.Manager):
    def active(self):
        """Get all the active accounts."""
        qs = self.get_queryset()
        return qs.filter(status__in=self.model.ACTIVE_STATUSES)


class Account(models.Model):
    """Account holds the user's state"""

    class Status(models.IntegerChoices):
        TRIALING = 1
        ACTIVE = 2
        EXEMPT = 3
        CANCELED = 4
        TRIAL_EXPIRED = 5

    ACTIVE_STATUSES = (Status.TRIALING, Status.ACTIVE, Status.EXEMPT)

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.TRIALING,
        db_index=True,
    )

    objects = AccountManager()


class User(AbstractUser):
    '''
        Custom user class so i can add other settings later or field to do user

    '''

    # customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL,
    #                              help_text="The user's Stripe Customer object, if it exists")
    # subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL,
    #                                  help_text="The user's Stripe Subscription object, if it exists")


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    """A new user gets an associated account."""
    if created:
        Account.objects.create(user=instance)
