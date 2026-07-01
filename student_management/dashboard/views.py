from django.shortcuts import render
from students.models import *
from courses.models import *
from enrollments.models import *
# Create your views here.

def dashboard(request):
    context = {
        "total_students": Student.objects.count() if request.user.is_authenticated else 0,
        "total_courses": Course.objects.count() if request.user.is_authenticated else 0,
        "active_enrollments":Enrollment.objects.count() if request.user.is_authenticated else 0
    }
    return render(request,'dashboard/dashboard.html',context)