from django.urls import path
from .views import client_login, acommodation_login, client_register, acommodation_register

app_name="users"

urlpatterns = [
    path('client/login', client_login, name='client_login'),
    path('client/register', client_register, name='client_register'),
    path('acommodation/login', acommodation_login, name='acommodation_login'),
    path('acommodation/register', acommodation_register, name='acommodation_register'),
]
