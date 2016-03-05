from django.db import models
from django.contrib.auth.models import User

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
genders = (
    ('M', 'M'),
    ('F', 'F'),
)


class Account(models.Model):

    customer = models.ForeignKey(User)
    account_number = models.IntegerField(default=gen_acc_num(), unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.CharField(max_length=10, choices=account_types)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.account_number)


class UserInfo(models.Model):

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.CharField(max_length=1000)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=genders)
    contact_number = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Transaction(models.Model):

    customer = models.ForeignKey(User)
    account_num = models.ForeignKey(Account, db_column="account_number", to_field="account_number")
    trans_type = models.CharField(max_length=10, choices=trans_types)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-time']


class RejectedInfo(models.Model):

    cust = models.ForeignKey(User)
    information = models.CharField(max_length=1000)


