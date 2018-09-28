from django.shortcuts import render

from django.views.generic import ListView, DetailView

from question.models import QAA, FAQ

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from femibox.views import LoginRequiredMixin


# Create your views here.

#--- ListView
class QAALV(ListView):
    model = QAA
    template_name = 'qaa/qaa_all.html'
    context_object_name = 'qaa'
    paginate_by = 10

class FAQLV(ListView):
    model = FAQ
    template_name = 'faq/faq_all.html'
    context_object_name = 'faq'
    paginate_by = 10

#--- DetailView
class QAADV(DetailView):
    model = QAA
    template_name = 'qaa/qaa_detail.html'

class FAQDV(DetailView):
    model = FAQ
    template_name = 'faq/faq_detail.html'

#--- FormView
class QAACreateView(LoginRequiredMixin, CreateView):
    model = QAA
    template_name = 'qaa/qaa_form.html'
    fields = ['author', 'password', 'title', 'content', 'image']
    success_url = reverse_lazy('question:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(QAACreateView, self).form_valid(form)

