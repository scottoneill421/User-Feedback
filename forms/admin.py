from django.contrib import admin

from .models import FeedbackFormModel

class FeedbackFormModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(FeedbackFormModel, FeedbackFormModelAdmin)
