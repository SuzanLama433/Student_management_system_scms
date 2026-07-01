from django.shortcuts import render, redirect
from .models import *
from students.models import *
from courses.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='log_in')
def enrollment_list(request):
    enrollments = Enrollment.objects.filter(is_deleted=False)
    return render(request,'enrollment_list.html',{'enrollments':enrollments})

@login_required(login_url='log_in')
def enrollment_form(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')
        enrollment_date = request.POST.get('enrollment_date')
        status = request.POST.get('status')

        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)

        Enrollment.objects.create(
            student=student,
            course=course,
            enrollment_date=enrollment_date,
            status=status,
        )
        messages.success(request,f'enrollment add sucessfully')
        

        return redirect('enrollment_list')

    return render(request, 'enrollment_form.html', {
        'students': students,
        'courses': courses,
    })
    
   


def enrollment_update(request, id):
    data = Enrollment.objects.get(id=id)

    students = Student.objects.filter(is_delete=False)
    courses = Course.objects.filter(is_deleted=False)

    if request.method == "POST":
        data.student_id = request.POST.get("student")
        data.course_id = request.POST.get("course")
        data.enrollment_date = request.POST.get("enrollment_date")
        data.status = request.POST.get("status")

        data.save()

        return redirect("enrollment_list")

    context = {
        "data": data,
        "students": students,
        "courses": courses,
    }

    return render(request, "enrollment_update.html", context)

def enrollment_delete(request,id):
    data = Enrollment.objects.get(id=id)
    data.is_deleted = True
    data.save()
    
    return redirect('enrollment_list')

def restoreEnrollment(request):
    enrollments = Enrollment.objects.filter(is_deleted=True)
    return render(request, 'restoreEnrollment.html', {'enrollments': enrollments})

def restoreItem_enrollment(request,id):
    data = Enrollment.objects.get(id = id)
    data.is_deleted = False
    data.save()
    return redirect('restoreEnrollment')

def delete_permanent(request,id):
    data = Enrollment.objects.get(id=id)
    data.delete()
    return redirect('restoreEnrollment')

def delete_all(request):
    data = Enrollment.objects.filter(is_deleted=True)
    data.delete()
    return redirect('restoreEnrollment')