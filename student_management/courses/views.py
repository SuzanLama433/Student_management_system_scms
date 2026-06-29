from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def course_list(request):
    data = Course.objects.filter(is_deleted = False)
    return render(request,'courses_list.html',{'courses':data})

def courses_form(request):
    if request.method == "POST":
        course_name= request.POST['course_name']
        duration = request.POST['duration']
        fee = request.POST['fee']
        description = request.POST['description']
        
        Course.objects.create(course_name=course_name,duration=duration,fee = fee,description=description)
        messages.success(request,f'{course_name} course is sucessfully added ')
        return redirect('course_form')
    return render(request,'course_form.html')

def course_update(request,id):
    data = Course.objects.get(id=id)
    if request.method == 'POST':
        data = Course.objects.get(id=id)
        data.course_name = request.POST['course_name']
        data.duration = request.POST['duration']
        data.fee = request.POST['fee']
        data.description = request.POST['description']
        data.save()
        return redirect('course_list')
        
    return render(request,'course_update.html',{'data':data})

def delete_data(request,id):
    data = Course.objects.get(id=id)
    data.is_deleted=True
    data.save()
    return redirect('course_list')

def restoreCourse(request):
    course = Course.objects.filter(is_deleted = True)
    return render(request, 'restoreCourse.html',{'courses':course})

def restoreItem_courses(request,id):
    data = Course.objects.get(id = id)
    data.is_deleted = False
    data.save()
    return redirect('restoreCourse')

def delete_permanent(request,id):
    data = Course.objects.get(id=id)
    data.delete()
    return redirect('restoreCourse')

def delete_all(request):
    data = Course.objects.filter(is_deleted=True)
    data.delete()
    return redirect('restoreCourse')