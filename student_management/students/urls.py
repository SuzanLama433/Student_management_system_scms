from django.urls import path
from .views import *

urlpatterns = [
    path('',students_list,name='list'),
    path('studentsform/',students_form,name='form'),
    path('deleteData/<int:id>/',delete_data,name='deleteData'),
    path('dataEdit/<int:id>/',edit_data,name='dataEdit'),
    path('restoreData/',restoreData,name='restoreData'),
    path('restoreItem/<int:id>',restoreItem,name='restoreItem'),
    path('deletePerma/<int:id>/',delete_permanent,name='delete_permanent'),
    path('deleteAll/',delete_all,name='delete_all')
]
