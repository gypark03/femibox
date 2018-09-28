from django.shortcuts import render

from django.views.generic import ListView, DetailView

from product.models import goods, box

from django.urls import reverse_lazy
from femibox.views import PageableMixin

# Create your views here.

#--- ListView
class GoodsLV(ListView):
    model = goods
    template_name = 'goods/goods_all.html'
    context_object_name = 'goods'
    
class BoxLV(ListView):
    model = box
    template_name = 'box/box_all.html'
    context_object_name = 'box'

#--- DetailView
class GoodsDV(DetailView):
    model = goods
    template_name = 'goods/goods_detail.html'
    
class BoxDV(DetailView):
    model = box
    template_name = 'box/box_detail.html'
    
