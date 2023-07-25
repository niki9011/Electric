from django.urls import path
from ..cars import views


urlpatterns = [
    path('cars/details/<int:pk>/', views.CarDetailsView.as_view(), name="car details"),
    path('cars/add/', views.CarAddView.as_view(), name="car add"),
    path('cars/update/<int:pk>/', views.CarUpdateView.as_view(), name="car update"),
    path('cars/delete/<int:pk>/', views.CarDeleteView.as_view(), name="car delete"),
    path('cars/', views.CarsListView.as_view(), name="new car"),
]