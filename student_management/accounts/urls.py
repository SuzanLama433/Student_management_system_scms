from django.urls import path
from .views import *
urlpatterns = [
    path('',log_in, name='log_in'),
    path("register/",register, name="register"),
    path('log_out/',log_out, name='log_out'),
    path('password_change/',password_change,name='password_change')
]
 