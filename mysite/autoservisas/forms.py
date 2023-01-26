from .models import UzsakymasReview, Profilis, UzsakymoEilute
from django import forms
from django.contrib.auth.models import User


class UzsakymasReviewForm(forms.ModelForm):
    class Meta:
        model = UzsakymasReview
        fields = ('content', 'order_line', 'reviewer')
        widgets = {'order_line': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {'username': forms.HiddenInput()}


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']


class DateInput(forms.DateInput):
    input_type = 'date'


class UserOrderCreateForm(forms.ModelForm):
    class Meta:
        model = UzsakymoEilute
        fields = ('kiekis', 'kaina', 'paslauga_id', 'grazinti_iki', 'uzsakymas_id')
        widgets = {'kaina': forms.HiddenInput, 'grazinti_iki': DateInput}