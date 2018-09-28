from django.shortcuts import render

from django.views.generic import ListView, DetailView

from campaign.models import Cam

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from femibox.views import LoginRequiredMixin
from femibox.views import PageableMixin

# Create your views here.

#--- ListView
class CamLV(PageableMixin, ListView):
    model = Cam
    template_name = 'campaign/campaign_all.html'
    context_object_name = 'campaign'

#--- DetailView
class CamDV(DetailView):
    model = Cam
    template_name = 'campaign/campaign_detail.html'

#--- FormView
class CamCreateView(LoginRequiredMixin, CreateView):
    model = Cam
    template_name = 'campaign/campaign_form.html'
    fields = ['author', 'title', 'content']
    success_url = reverse_lazy('campaign:campaign_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CamCreateView, self).form_valid(form)
