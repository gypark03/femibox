from django.shortcuts import render

from django.views.generic import ListView, DetailView

from femiLetter.models import Memos

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from femibox.views import LoginRequiredMixin
from femibox.views import PageableMixin

# Create your views here.

#--- ListView
class LetterLV(PageableMixin, ListView):
    model = Memos
    template_name = 'femiLetter/letter.html'
    context_object_name = 'femiLetter'

#--- DetailView
class LetterDV(DetailView):
    model = Memos
    template_name = 'femiLetter/letter_detail.html'

#--- FormView
class LetterCreateView(LoginRequiredMixin, CreateView):
    model = Memos
    template_name = 'femiLetter/letter_form.html'
    fields = ['author', 'title', 'content', 'image']
    success_url = reverse_lazy('femiLetter:letter_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(LetterCreateView, self).form_valid(form)

