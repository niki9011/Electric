from django.urls import path
from .views import send_email, contact


urlpatterns = [

    path('send_email/', send_email, name="send email"),
    path('contact/', contact, name="contact"),
]
