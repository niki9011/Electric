from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from electrical_drive.accounts.views import profile, RegisterUserView, EditUpdateView


urlpatterns = [
    path('accounts/change-password/', EditUpdateView,
         name="change_password"),
    path('accounts/change-password-done/', PasswordChangeDoneView.as_view(template_name='accounts/change-password-done.html'),
         name="password_change_done"),
    path('profile/', profile, name="profile"),
    path("register/", RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(template_name='accounts/login_user.html'), name='login user'),
    path('logout/', LogoutView.as_view(template_name='home/site.html'), name='logout user'),

]
