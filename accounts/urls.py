from django.conf.urls import url
from accounts.views import *

urlpatterns = [
    url(r'^register/$', UserAgreeView.as_view(), name='register'),
    url(r'^register/join/$', SignUpView.as_view(), name='join'),
]