from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Customer(models.Model):
    owner = models.OneToOneField(User, related_name='customer')
    plate_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return '{}'.format(self.owner.username)


class Message(models.Model):
    sender = models.ForeignKey(Customer, related_name='sender')
    plate = models.CharField(max_length=15, default='')
    content = models.TextField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} -> {}'.format(self.sender, self.plate)
