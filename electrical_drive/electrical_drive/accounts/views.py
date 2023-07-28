from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from electrical_drive.accounts.forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm, ProfileCreateForm
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views


from .models import Profile


def profile(request):
    form = UserUpdateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'accounts/user_profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileUpdateForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile')

    context = {"form": form}
    return render(request, "accounts/change-password.html", context)


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm

    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'


class EditUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "accounts/change-password.html"
    fields = "__all__"
    success_url = reverse_lazy("home page")