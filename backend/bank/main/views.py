from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import Transaction
from .models import Account


class Home(TemplateView):
    """Create the home page for when a user logs in and display their summary info"""
    template_name = 'main/home.html'


class CreateTransaction(CreateView):
    """Allow a user to create a transaction, either deposit or withdraw with a specific amount"""
    model = Transaction
    fields = ['trans_type', 'amount', 'description']

    def form_valid(self, form):
        """Validate if the user has the correct balance to perform the following action"""
        data = form.save(commit=False)
        account = Account.objects.get(customer=self.request.user)
        data.customer = self.request.user
        data.account_num = account
        if data.trans_type == 'Withdraw':
            if data.amount > account.balance:
                return render(self.request, 'errors/invalid_transaction.html')
            else:
                new_balance = account.balance - data.amount
                Account.objects.filter(customer=self.request.user).update(balance=new_balance)
        else:
            new_balance = account.balance + data.amount
            Account.objects.filter(customer=self.request.user).update(balance=new_balance)
        data.save()
        return redirect(reverse('successful_transaction'))


class SuccessfulTransaction(TemplateView):
    """Let the user know the transaction was successful"""
    template_name = 'success/successful_transaction.html'


class SetupAccount(CreateView):
    """Allow the user to create a new bank account"""
    model = Account
    fields = ['balance', 'account_type']

    def get_success_url(self):
        """Let the user know their bank account was created successfully"""
        return redirect(reverse('successful_creation'))


class SuccessfulCreation(TemplateView):
    """Let the user know the creation was successful"""
    template_name = 'success/successful_creation'
