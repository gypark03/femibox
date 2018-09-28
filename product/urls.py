from django.conf.urls import url
from product.views import *

app_name = 'product'

urlpatterns = [
    # Example: /goods
    url(r'^goods/$', GoodsLV.as_view(), name='goods_list'),

    # Example: /goods/detail
    url(r'^goods/(?P<pk>\d+)/$', GoodsDV.as_view(), name='goods_detail'),
    
    # Example: /box
    url(r'^box/$', BoxLV.as_view(), name='box_list'),

    # Example: /box/detail
    url(r'^box/(?P<pk>\d+)/$', BoxDV.as_view(), name='box_detail'),
]
