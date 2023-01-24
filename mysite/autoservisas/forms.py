from .models import UzsakymasReview
from django import forms


class UzsakymasReviewForm(forms.ModelForm):
    class Meta:
        model = UzsakymasReview
        fields = ('content', 'order_line', 'reviewer')
        widgets = {'order_line': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}
