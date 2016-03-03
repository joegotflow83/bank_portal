from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

import random

# Helper Functions
def gen_acc_num():
    """Generate a account number"""
    num = [random.randrange(0, 10) for x in range(13)]
    return ''.join(map(str, num))

# Choice Field for bank account type
account_types = (
    ('Checking', 'Checking'),
    ('Savings', 'Savings'),
)
trans_types = (
    ('Withdraw', 'Withdraw'),
    ('Deposit', 'Deposit'),
)


class Account(models.Model):

    customer = models.ForeignKey(User)
    account_number = models.IntegerField(default=gen_acc_num())
    balance = models.FloatField(validators=[MinValueValidator(200.00)])
    account_type = models.CharField(max_length=10, choices=account_types)


class UserInfo(models.Model):

    user = models.OneToOneField(User)
    account_num = models.ForeignKey(Account)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.CharField(max_length=1000)
    email = models.EmailField()
    sex = models.CharField(max_length=1)
    contact_number = models.IntegerField()


class Transaction(models.Model):

    account_num = models.ForeignKey(Account)
    customer = models.ForeignKey(User)
    trans_type = models.CharField(max_length=10, choices=trans_types)
    amount = models.FloatField()
    description = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)


class RejectedInfo(models.Model):

    cust = models.ForeignKey(User)
    information = models.CharField(max_length=1000)


