from django.shortcuts import redirect, render
from electrical_drive.accounts.forms import RegisterUserForm, UserUpdateForm
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy
from django.views import generic as views


def profile(request):
    form = UserUpdateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'accounts/user_profile.html', context)


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

