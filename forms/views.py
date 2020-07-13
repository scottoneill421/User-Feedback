from django.views.generic.edit import FormView
from .forms import FeedbackForm

class FeedbackFormView(FormView):
    template_name = 'FeedbackForm.html'
    form_class = FeedbackForm
    success_url = '/thanks/'
