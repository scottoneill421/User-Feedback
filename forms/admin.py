from django.contrib import admin

from .models import SubmittedForm

class SubmittedFormAdmin(admin.ModelAdmin):
    pass

admin.site.register(SubmittedForm, SubmittedFormAdmin)
