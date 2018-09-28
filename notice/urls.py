from django.conf.urls import url
from notice.views import *

app_name = 'notice'

urlpatterns = [
    url(r'^$', noticeLV.as_view(), name='index'),

    url(r'^notice/$', noticeLV.as_view(), name='notice_list'),

    url(r'^notice/(?P<pk>\d+)/$', noticeDV.as_view(), name='notice_detail'),
]
