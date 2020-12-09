from django.urls import path
from app import views

urlpatterns = [
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]