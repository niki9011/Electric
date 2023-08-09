from django import forms
from .models import AllNews


class NewsForm(forms.ModelForm):
    class Meta:
        model = AllNews
        fields = "__all__"
