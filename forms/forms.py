from django.forms import ModelForm
from .models import FeedbackFormModel

class FeedbackForm(ModelForm):

    class Meta:
        model = FeedbackFormModel
        fields = ("subject", "author", "body", "screenshot",)
