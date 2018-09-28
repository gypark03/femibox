from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from accounts.forms import UserCreationMultiForm
from django.urls import reverse_lazy

# Create your views here.

#--- UserCreation
class UserAgreeView(TemplateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('join')

class SignUpView(CreateView):
    template_name = 'registration/join.html'
    form_class = UserCreationMultiForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()
        return redirect(self.success_url)