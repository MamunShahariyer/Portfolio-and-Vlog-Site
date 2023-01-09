

from django.urls import path
from . import views

app_name = 'userinfo_app'

urlpatterns = [
    path('users/', views.home, name='userinfo_home'),

]
