from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    url(r'^home/$', login_required(views.Home.as_view()), name='home'),
    url(r'^create_transaction/(?P<number>\d+)/$', views.CreateTransaction.as_view(), name='create_transaction'),
    url(r'^account_transactions/(?P<number>\d+)/$', views.TransactionList.as_view(), name='transaction_list'),
    url(r'^setup_info/$', views.SetupInfo.as_view(), name='setup_info'),
    url(r'^setup_account/$', views.SetupAccount.as_view(), name='setup_account'),
    url(r'^successful_transaction/$', views.SuccessfulTransaction.as_view(), name='successful_transaction'),
    url(r'^update_info/(?P<pk>\d+)/$', views.UpdateInfo.as_view(), name='update_info'),
    url(r'^account_transfer/(?P<number>\d+)/$', views.CreateTransfer.as_view(), name='transfer'),
    url(r'^successful_transfer/$', views.SuccessfulTransfer.as_view(), name='successful_transfer'),
    url(r'^invalid_transfer/$', views.InvalidTransfer.as_view(), name='invalid_transfer'),
]
