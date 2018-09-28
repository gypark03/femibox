from django.conf.urls import url
from femiLetter.views import *

app_name = 'femiLetter'

urlpatterns = [
    # Example: /
    url(r'^$', LetterLV.as_view(), name='index'),

    # Example: /letter
    url(r'^letter/$', LetterLV.as_view(), name='letter_list'),

    # Example: /letter/detail
    url(r'^letter/(?P<pk>\d+)/$', LetterDV.as_view(), name='letter_detail'),

    # Example: /add/
    url(r'^add/$',
        LetterCreateView.as_view(), name="add",
    ),
]
