from django import forms

from electrical_drive.news.models import Allnews


class NewsForm(forms.ModelForm):
    class Meta:
        model = Allnews
        fields = "__all__"
