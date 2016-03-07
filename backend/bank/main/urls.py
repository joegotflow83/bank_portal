from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^home/$', login_required(views.Home.as_view()), name='home'),
    url(r'^create_transaction/(?P<number>\d+)/$', login_required(views.CreateTransaction.as_view()), name='create_transaction'),
    url(r'^account_transactions/(?P<number>\d+)/$', login_required(views.TransactionList.as_view()), name='transaction_list'),
    url(r'^transaction_detail/(?P<pk>\d+)/$', login_required(views.TransactionDetail.as_view()), name='transaction_detail'),
    url(r'^setup_info/$', login_required(views.SetupInfo.as_view()), name='setup_info'),
    url(r'^setup_account/$', login_required(views.SetupAccount.as_view()), name='setup_account'),
    url(r'^successful_transaction/$', login_required(views.SuccessfulTransaction.as_view()), name='successful_transaction'),
    url(r'^update_info/(?P<pk>\d+)/$', login_required(views.UpdateInfo.as_view()), name='update_info'),
    url(r'^account_transfer/(?P<number>\d+)/$', login_required(views.CreateTransfer.as_view()), name='transfer'),
    url(r'^invalid_transfer/$', login_required(views.InvalidTransfer.as_view()), name='invalid_transfer'),
    url(r'^disable_account_success/(?P<number>\d+)/$', login_required(views.DisableAccount.as_view()), name='disable_account'),
    url(r'^reactivate_account_success/(?P<number>\d+)/$', login_required(views.ReactivateAccount.as_view()), name='reactivate_account'),
    url(r'^remove_account/(?P<number>\d+)/$', views.DeleteAccount.as_view(), name='delete'),
    url(r'^rejected_transactions/$', views.RejectedList.as_view(), name='rejects'),
]
