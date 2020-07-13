from django.urls import path
from .views import FeedbackFormView

urlpatterns = [
    path('', FeedbackFormView.as_view()),
]
