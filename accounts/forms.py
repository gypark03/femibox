from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile

from betterforms.multiform import MultiModelForm

class HorizontalRadioSelect(forms.RadioSelect):
    template_name = 'horizontal_select.html'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth', 'gender', 'phone', ]
        widgets = {
            'gender': HorizontalRadioSelect(),
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=12)
    email = forms.EmailField(max_length=254, help_text='ex) aaa@aaaa.com')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2', 'email', ]

class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': SignUpForm,
        'profile': ProfileForm,
    }