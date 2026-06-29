from django.shortcuts import render
from students.models import *
from courses.models import *
from enrollments.models import *
# Create your views here.

def dashboard(request):
    context = {
        "total_students": Student.objects.count(),
        "total_courses": Course.objects.count(),
        "active_enrollments":Enrollment.objects.count()
    }
    return render(request,'dashboard/dashboard.html',context)