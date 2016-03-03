from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from accounts import views

urlpatterns = [
    url(r'^login/', auth_views.login, name='login'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^logout/$', login_required(auth_views.logout_then_login), name='logout')
]
