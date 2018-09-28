from django.conf.urls import url
from campaign.views import *

app_name = 'campaign'

urlpatterns = [
    # Example: /
    url(r'^$', CamLV.as_view(), name='index'),

    # Example: /campaign
    url(r'^campaign/$', CamLV.as_view(), name='campaign_list'),

    # Example: /campaign/detail
    url(r'^campaign/(?P<pk>\d+)/$', CamDV.as_view(), name='campaign_detail'),

    # Example: /add/
    url(r'^campaign/(?P<pk>\d+)/$',
        CamCreateView.as_view(), name="campaign_form",
    ),
]
