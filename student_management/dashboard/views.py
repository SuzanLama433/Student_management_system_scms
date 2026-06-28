from django.shortcuts import render
from students.models import *
# Create your views here.

def dashboard(request):
    total_students = Student.objects.count()
    
    return render(request,'dashboard/dashboard.html',{'total_students':total_students})