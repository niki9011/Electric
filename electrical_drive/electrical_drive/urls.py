from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("electrical_drive.motors.urls")),
    path("", include("electrical_drive.accounts.urls")),
    path("", include("electrical_drive.home.urls")),
    path("", include("electrical_drive.contact.urls")),
    path("", include("electrical_drive.cars.urls")),
    path("", include("electrical_drive.news.urls")),
    path("", include("electrical_drive.about.urls")),
    path("", include("electrical_drive.scooters.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
