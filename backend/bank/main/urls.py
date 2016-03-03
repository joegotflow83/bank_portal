from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    url(r'^home/$', login_required(views.Home.as_view()), name='home'),
    url(r'^create_transaction/$', views.CreateTransaction.as_view(), name='create_transaction'),
    url(r'^setup_account/$', views.SetupAccount.as_view(), name='setup_account'),
    url(r'^successful_transaction/$', views.SuccessfulTransaction.as_view(), name='successful_transaction'),
    url(r'^successful_creation/$', views.SuccessfulCreation.as_view(), name='successful_creation'),
]
