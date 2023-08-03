from django import forms
from .models import Scooters


class ScooterForm(forms.ModelForm):
    class Meta:
        model = Scooters
        fields = "__all__"
