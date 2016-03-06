from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('score', 'comment', 'note', 'proposal', 'reviewer' )
        widgets = {
            'proposal': forms.HiddenInput(),
            'reviewer': forms.HiddenInput(),
        }