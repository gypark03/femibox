from django.views.generic.base  import TemplateView
from django.views.generic import ListView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from notice.models import notice
from femiLetter.models import Memos
from campaign.models import Cam

from django.contrib.auth.decorators import login_required

import logging

#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'
    
    #--- 메인에 띄우기 위해
    def femiLetter(self):
        return Memos.objects.order_by('-create_date')[:4]

    def notice(self):
        return notice.objects.order_by('-create_date')[:7]

    def Cam(self):
        return Cam.objects.order_by('-create_date')[:1]


class AboutView(TemplateView):
    template_name = 'about.html'

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class PageableMixin(object):
    logger = logging.getLogger(__name__)
    paginate_by = 8
    block_size = 5

    def get_context_data(self, **kwargs):
        self.logger.debug('PageableMixin.get_context_data()')
        context = super(PageableMixin, self).get_context_data(**kwargs)

        start_index = int((context['page_obj'].number - 1) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))

        context['page_range'] = context['paginator'].page_range[start_index:end_index]

        return context
