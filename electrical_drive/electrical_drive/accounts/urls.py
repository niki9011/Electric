from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from electrical_drive.accounts.views import RegisterUserView, ProfileUserView

urlpatterns = [
    path('profile/', ProfileUserView.as_view(), name="profile"),
    path("register/", RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(template_name='accounts/login_user.html'), name='login user'),
    path('logout/', LogoutView.as_view(template_name='home/site.html'), name='logout user'),
]