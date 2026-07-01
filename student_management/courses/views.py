from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


# Display all active courses
@login_required(login_url='log_in')
def course_list(request):
    # Get all courses that are not soft deleted
    data = Course.objects.filter(is_deleted=False)

    # Render course list page
    return render(request, 'courses_list.html', {'courses': data})


# Display course form and save a new course
@login_required(login_url='log_in')
def courses_form(request):
    # Check if the form is submitted
    if request.method == "POST":
        # Get form data
        course_name = request.POST['course_name']
        duration = request.POST['duration']
        fee = request.POST['fee']
        description = request.POST['description']

        # Create a new course
        Course.objects.create(
            course_name=course_name,
            duration=duration,
            fee=fee,
            description=description
        )

        # Display success message
        messages.success(request, f'{course_name} course is sucessfully added ')

        # Redirect back to the course form
        return redirect('course_form')

    # Display course form page
    return render(request, 'course_form.html')


# Update an existing course
def course_update(request, id):
    # Get course by ID
    data = Course.objects.get(id=id)

    # Check if update form is submitted
    if request.method == 'POST':
        data = Course.objects.get(id=id)

        # Update course information
        data.course_name = request.POST['course_name']
        data.duration = request.POST['duration']
        data.fee = request.POST['fee']
        data.description = request.POST['description']

        # Save updated course
        data.save()

        # Redirect to course list
        return redirect('course_list')

    # Display update form with existing course data
    return render(request, 'course_update.html', {'data': data})


# Soft delete a course
def delete_data(request, id):
    # Get course by ID
    data = Course.objects.get(id=id)

    # Mark course as deleted
    data.is_deleted = True
    data.save()

    # Redirect to course list
    return redirect('course_list')


# Display all soft deleted courses
def restoreCourse(request):
    # Get all deleted courses
    course = Course.objects.filter(is_deleted=True)

    # Render restore course page
    return render(request, 'restoreCourse.html', {'courses': course})


# Restore a soft deleted course
def restoreItem_courses(request, id):
    # Get course by ID
    data = Course.objects.get(id=id)

    # Restore the course
    data.is_deleted = False
    data.save()

    # Redirect to restore page
    return redirect('restoreCourse')


# Permanently delete a single course
def delete_permanent(request, id):
    # Get course by ID
    data = Course.objects.get(id=id)

    # Permanently delete the course
    data.delete()

    # Redirect to restore page
    return redirect('restoreCourse')


# Permanently delete all soft deleted courses
def delete_all(request):
    # Get all deleted courses
    data = Course.objects.filter(is_deleted=True)

    # Permanently delete all deleted courses
    data.delete()

    # Redirect to restore page
    return redirect('restoreCourse')