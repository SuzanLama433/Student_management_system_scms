from django.urls import path
from .views import *
urlpatterns = [
    path('',course_list,name='course_list'),
    path('course_form/',courses_form,name='course_form'),
    path('course_update/<int:id>/', course_update, name='course_update'),
    path('deleteData/<int:id>/', delete_data, name='course_delete'),
    path('restoreCourse/',restoreCourse,name='restoreCourse'),
    path('restoreItems_courses/<int:id>/',restoreItem_courses,name='restoreItems_courses'),
    path('deletePerma/<int:id>/',delete_permanent,name='deletePerma'),
    path('deleteAll/',delete_all,name='deleteAll')
]