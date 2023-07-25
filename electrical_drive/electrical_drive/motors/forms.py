from django import forms

from electrical_drive.motors.models import Bikes


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bikes
        fields = "__all__"
