from django.urls import path
from . import views

app_name = 'revos_app'

urlpatterns = [
    path('', views.index, name='index'),
]