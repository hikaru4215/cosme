from django.urls import path
from app import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('dryskin/', views.DryskinView.as_view(), name='dryskin'),
	path('oilyskin', views.OilyskinView.as_view(), name='oilyskin'),
	path('mixskin', views.MixskinView.as_view(), name='mixskin'),
	path('normal', views.NormalskinView.as_view(), name='normalskin'),
	path('skin_feature', views.SkinFeatureView.as_view(), name='skin_feature'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]