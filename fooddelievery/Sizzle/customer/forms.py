from .models import Feedback
from django import forms
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email','phone', 'comments']

    def clean_comments(self):
        comments = self.cleaned_data.get('comments')
        if len(comments) > 150:
            raise forms.ValidationError("Comments cannot exceed 150 characters.")
        return comments