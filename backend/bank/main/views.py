from django.shortcuts import render, get_list_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from datetime import datetime, timedelta

from .models import Transaction, Account, UserInfo, RejectedInfo


class Index(TemplateView):
    """Display this page when users first access the site"""
    template_name = 'guest/index.html'


class About(TemplateView):
    """Display information about the company"""
    template_name = 'guest/about.html'


class Home(TemplateView):
    """Create the home page for when a user logs in and display their summary info"""
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        """Grab the users data to display on their dashboard"""
        context = super().get_context_data(**kwargs)
        context['accounts'] = Account.objects.filter(customer=self.request.user)
        context['userinfo'] = UserInfo.objects.filter(user=self.request.user)
        return context


class CreateTransaction(CreateView):
    """Allow a user to create a transaction, either deposit or withdraw with a specific amount"""
    model = Transaction
    fields = ['trans_type', 'amount', 'description']

    def form_valid(self, form):
        """Validate if the user has the correct balance to perform the following action"""
        data = form.save(commit=False)
        account = Account.objects.get(account_number=self.kwargs['number'])
        data.customer = self.request.user
        data.account_num = account
        if data.trans_type == 'Withdraw':
            if data.amount > account.balance:
                RejectedInfo.objects.create(cust=self.request.user, information='Withdraw more than account has.')
                return render(self.request, 'errors/invalid_transaction.html')
            else:
                new_balance = account.balance - data.amount
                data.current_balance = new_balance
                Account.objects.filter(customer=self.request.user).update(balance=new_balance)
        else:
            new_balance = account.balance + data.amount
            data.current_balance = new_balance
            Account.objects.filter(customer=self.request.user).update(balance=new_balance)
        data.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Let users know their creation was successful"""
        return reverse('successful_transaction')


class SuccessfulTransaction(TemplateView):
    """Let the user know the transaction was successful"""
    template_name = 'success/successful_transaction.html'


class SetupAccount(CreateView):
    """Allow the user to create a new bank account"""
    model = Account
    fields = ['balance', 'account_type']

    def form_valid(self, form):
        """Validate the form"""
        data = form.save(commit=False)
        data.customer = self.request.user
        data.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Let the user know their bank account was created successfully"""
        return reverse('home')


class SuccessfulCreation(TemplateView):
    """Let the user know the creation was successful"""
    template_name = 'success/successful_creation'


class SetupInfo(CreateView):
    """Allow a user to create their user info"""
    model = UserInfo
    fields = ['first_name', 'last_name', 'address', 'email', 'sex', 'contact_number']

    def form_valid(self, form):
        """Validate the form"""
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect the user to their dashboard"""
        return reverse('home')


class UpdateInfo(UpdateView):
    """Allow a user to update their user info"""
    model = UserInfo
    template_name = 'main/update_userinfo.html'
    fields = ['first_name', 'last_name', 'address', 'email', 'contact_number']

    def form_valid(self, form):
        """Validate the form"""
        data = form.save(commit=True)
        data.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect user to dashboard"""
        return reverse('home')


class TransactionList(ListView):
    """View an account in detail"""
    model = Transaction
    template_name = 'main/transaction_list.html'

    def get_queryset(self):
        return get_list_or_404(Transaction, account_num=self.kwargs['number'],
                               time__gte=datetime.now()-timedelta(days=30))


class TransactionDetail(DetailView):
    """View a transaction in detail"""
    model = Transaction

    def get_queryset(self):
        return Transaction.objects.filter(customer=self.request.user)


class CreateTransfer(CreateView):
    """Allow a user to transfer money between bank account"""
    model = Transaction
    fields = ['account_num', 'amount']
    template_name = 'main/transfer.html'

    def form_valid(self, form):
        """Validate the form"""
        data = form.save(commit=False)
        data.customer = self.request.user
        withdraw_account = Account.objects.get(account_number=self.kwargs['number'])
        if data.account_num == withdraw_account:
            RejectedInfo.objects.create(cust=self.request.user, information='Transfer between the same account.')
            return redirect(reverse('invalid_transfer'))
        elif data.amount > withdraw_account.balance:
            RejectedInfo.objects.create(cust=self.request.user, information='Over draw on account')
            return redirect(reverse('invalid_transfer'))
        withdraw_account_balance = withdraw_account.balance - data.amount
        Account.objects.filter(account_number=self.kwargs['number']).update(balance=withdraw_account_balance)
        deposit_account_balance = data.account_num.balance + data.amount
        Account.objects.filter(account_number=data.account_num.account_number).update(balance=deposit_account_balance)
        data.current_balance = deposit_account_balance
        data.description = 'Transfer'
        data.trans_type = 'Deposit'
        Transaction.objects.create(customer=self.request.user, account_num=withdraw_account,
                                   trans_type='Withdraw', current_balance=withdraw_account_balance,
                                   amount=data.amount, description='Transfer', time=datetime.now())
        data.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect the user to the successful page"""
        return reverse('home')


class InvalidTransfer(TemplateView):
    """Let the user know that is a invalid transfer"""
    template_name = 'errors/invalid_transfer.html'


class DisableAccount(View):
    """Disable the users account"""
    def get(self, request, number):
        Account.objects.filter(account_number=number).update(active=False)
        return render(request, 'success/disable.html')


class ReactivateAccount(View):
    """Reactivate the users account"""
    def get(self, request, number):
        Account.objects.filter(account_number=number).update(active=True)
        return render(request, 'success/reactivate.html')


class DeleteAccount(View):
    """Delete the users bank account"""
    def get(self, request, number):
        account = Account.objects.get(account_number=self.kwargs['number'])
        if account.balance > 0:
            RejectedInfo.objects.create(cust=request.user, information='Delete account with money left in account.')
            return render(request, 'errors/invalid_deletion.html')
        account.delete()
        return render(request, 'success/destroy.html')


class RejectedList(ListView):
    """Display rejected transactions on users accounts"""
    model = RejectedInfo
