from django.conf.urls import url
from question.views import *

app_name = 'question'

urlpatterns = [
    # Example: /
    url(r'^$', QAALV.as_view(), name='index'),

    # Example: /qaa
    url(r'^qaa/$', QAALV.as_view(), name='QAA_list'),

    # Example: /qaa/detail
    url(r'^qaa/(?P<pk>\d+)/$', QAADV.as_view(), name='QAA_detail'),
    
    # Example: /faq
    url(r'^faq/$', FAQLV.as_view(), name='FAQ_list'),

    # Example: /faq/detail
    url(r'^faq/(?P<pk>\d+)/$', FAQDV.as_view(), name='FAQ_detail'),

    # Example: /add/
    url(r'^add/$',
        QAACreateView.as_view(), name="add",
    ),
]
