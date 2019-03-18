from django.urls import path
from . import views

app_name = 'livepoll'

urlpatterns = [
    path('', views.random_num, name='random_num'),
    path('home/', views.HomePageView.as_view(), name='home'),
]
