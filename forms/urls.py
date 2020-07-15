from django.urls import path
from .views import FeedbackFormView, ThanksView

urlpatterns = [
    path('', FeedbackFormView.as_view()),
    path('thanks/', ThanksView.as_view()),
]
