from django.urls import path
from .views import HomePageView, AboutPageView # new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
	path('', HomePageView.as_view(), name='home'),
    path('../messages', HomePageView.as_view(), name='messages'),
    path('../admin', HomePageView.as_view(), name='admin'),
]