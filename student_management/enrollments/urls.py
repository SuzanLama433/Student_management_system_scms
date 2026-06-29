from django.urls import path
from .views import *
urlpatterns = [
    path('',enrollment_list,name='enrollment_list'),
    path('enrollment_form/',enrollment_form,name='enrollment_form'),
    path('enrollment_update/<int:id>/',enrollment_update,name='enrollment_update'),
    path('restoreEnrollment/', restoreEnrollment, name='restoreEnrollment'),
    path('enrollment_delete/<int:id>/', enrollment_delete, name='enrollment_delete'),
    path('restoreItem_enrollment/<int:id>/', restoreItem_enrollment, name='restoreItem_enrollment'),
    path('delete_permanent/<int:id>/', delete_permanent, name='delete_permanent'),
    path('delete_all/', delete_all, name='delete_all'),
]
