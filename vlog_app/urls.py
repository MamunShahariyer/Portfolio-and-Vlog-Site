

from django.urls import path
from . import views

app_name = 'vlog_app'

urlpatterns = [
    path('vlog/', views.home, name='vlog_home'),

]
