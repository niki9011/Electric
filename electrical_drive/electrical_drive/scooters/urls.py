from django.urls import path
from ..scooters import views

urlpatterns = [
    path('scooters/details/<int:pk>/', views.ScooterDetailsView.as_view(), name="scooter details"),
    path('scooters/add/', views.ScooterAddView.as_view(), name="scooter add"),
    path('scooters/update/<int:pk>/', views.ScooterUpdateView.as_view(), name="scooter update"),
    path('scooters/delete/<int:pk>/', views.ScooterDeleteView.as_view(), name="scooter delete"),
    path('scooters/', views.ScootersListView.as_view(), name="new scooter"),
]