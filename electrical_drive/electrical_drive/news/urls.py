from django.urls import path
from ..news import views


urlpatterns = [
    path('news/details/<int:pk>/', views.NewsDetailsView.as_view(), name="news details"),
    path('news/add/', views.NewsAddView.as_view(), name="news add"),
    path('news/update/<int:pk>/', views.NewsUpdateView.as_view(), name="news update"),
    path('news/delete/<int:pk>/', views.NewsDeleteView.as_view(), name="news delete"),
    path('news/', views.AllnewsListView.as_view(), name="new news"),
]