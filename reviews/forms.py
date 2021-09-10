from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Here you can write your review', 'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Review
        fields = ['text']
