from django.shortcuts import render

from django.views.generic import ListView, DetailView

from notice.models import notice

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

#--- ListView
class noticeLV(ListView):
    model = notice
    template_name = 'notice/notice_all.html'
    context_object_name = 'notice'

        

#--- DetailView
class noticeDV(DetailView):
    model = notice
    template_name = 'notice/notice_detail.html'
