from django.urls import path
from .views import HomePageView, DetailPageView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', DetailPageView.as_view(), name='post'),
    
    # to connect with the Pages app.
    path('../', HomePageView.as_view(), name='pages'),
    
    # to connect with the Pages app.
    path('../about', HomePageView.as_view(), name='about'),
    
    # to let the user log in.
    path('../admin', HomePageView.as_view(), name='admin'),
]