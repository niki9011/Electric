from django.urls import path
from ..motors import views


urlpatterns = [
    path('motors/details/<int:pk>/', views.BikeDetailsView.as_view(), name="bike details"),
    path('motors/add/', views.BikeAddView.as_view(), name="bike add"),
    path('motors/update/<int:pk>/', views.BikeUpdateView.as_view(), name="bike update"),
    path('motors/delete/<int:pk>/', views.BikeDeleteView.as_view(), name="bike delete"),
    path('motors/', views.BikesListView.as_view(), name="new bike"),
]