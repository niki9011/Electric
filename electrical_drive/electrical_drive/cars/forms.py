from django import forms
from electrical_drive.cars.models import Cars


class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"