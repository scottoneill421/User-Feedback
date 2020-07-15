from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import FeedbackForm

class FeedbackFormView(FormView):
    template_name = 'FeedbackForm.html'
    form_class = FeedbackForm
    success_url = "/thanks/"

    def form_valid(self, form):
        form.instance.save()
        return HttpResponseRedirect(self.success_url)


class ThanksView(TemplateView):
    template_name = 'thanks.html'
