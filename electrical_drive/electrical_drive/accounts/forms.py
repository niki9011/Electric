from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()
    first_name = forms.CharField(
        max_length=30,
        required=True
    )

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('It works')

    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    # picture = forms.URLField()
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

