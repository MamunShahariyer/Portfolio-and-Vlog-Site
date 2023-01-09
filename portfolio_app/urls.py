

from django.urls import path
from . import views

app_name = 'portfolio_app'

urlpatterns = [
    path('', views.home, name='portfolio_home'),
    path('aboutme', views.aboutme, name='aboutme'),


]
