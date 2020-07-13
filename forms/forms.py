from django import forms

class FeedbackForm(forms.Form):
    subject = forms.CharField(label="Error Type", max_length=50)
    author = forms.CharField(label="Your Name", max_length=250)
    body = forms.CharField(label="Description",
                           widget=forms.Textarea(
                                  attrs={
                                      "rows": 30,
                                  }
                               )
                            )
    screenshot = forms.ImageField(required=False)
