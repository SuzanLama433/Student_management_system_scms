from django.urls import path
from .views import *
urlpatterns = [
    path('',course_list,name='course_list'),
    path('course_form/',courses_form,name='course_form'),
    path('course_update/<int:id>/', course_update, name='course_update'),
    path('deleteData/<int:id>/', delete_data, name='course_delete')
]