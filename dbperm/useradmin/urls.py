from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'useradmin'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),    
    path('login/', views.LoginView.as_view(), name='login')
]