from django.http import HttpResponseRedirect

from django.views.generic import CreateView, TemplateView


from .forms import FeedbackForm
from .models import FeedbackFormModel

class FeedbackFormView(CreateView):
    model = FeedbackFormModel
    template_name = 'FeedbackForm.html'
    form_class = FeedbackForm
    success_url = "/thanks/"


class ThanksView(TemplateView):
    template_name = 'thanks.html'
