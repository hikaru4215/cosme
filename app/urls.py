from django.urls import path
from app import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]