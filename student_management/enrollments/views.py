from django.shortcuts import render, redirect
from .models import *
from students.models import *
from courses.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


# Display all active enrollments
@login_required(login_url='log_in')
def enrollment_list(request):
    # Get all enrollments that are not soft deleted
    enrollments = Enrollment.objects.filter(is_deleted=False)

    # Render enrollment list page
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})


# Display enrollment form and create a new enrollment
@login_required(login_url='log_in')
def enrollment_form(request):
    # Get all students and courses for dropdown lists
    students = Student.objects.all()
    courses = Course.objects.all()

    # Check if form is submitted
    if request.method == "POST":
        # Get form data
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')
        enrollment_date = request.POST.get('enrollment_date')
        status = request.POST.get('status')

        # Retrieve selected student and course objects
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)

        # Create a new enrollment
        Enrollment.objects.create(
            student=student,
            course=course,
            enrollment_date=enrollment_date,
            status=status,
        )

        # Display success message
        messages.success(request, 'enrollment add sucessfully')

        # Redirect to enrollment list
        return redirect('enrollment_list')

    # Display enrollment form page
    return render(request, 'enrollment_form.html', {
        'students': students,
        'courses': courses,
    })


# Update an existing enrollment
def enrollment_update(request, id):
    # Get enrollment by ID
    data = Enrollment.objects.get(id=id)

    # Get active students and courses for dropdown lists
    students = Student.objects.filter(is_delete=False)
    courses = Course.objects.filter(is_deleted=False)

    # Check if update form is submitted
    if request.method == "POST":
        # Update enrollment details
        data.student_id = request.POST.get("student")
        data.course_id = request.POST.get("course")
        data.enrollment_date = request.POST.get("enrollment_date")
        data.status = request.POST.get("status")

        # Save updated enrollment
        data.save()

        # Redirect to enrollment list
        return redirect("enrollment_list")

    # Pass data to the template
    context = {
        "data": data,
        "students": students,
        "courses": courses,
    }

    # Render update page
    return render(request, "enrollment_update.html", context)


# Soft delete an enrollment
def enrollment_delete(request, id):
    # Get enrollment by ID
    data = Enrollment.objects.get(id=id)

    # Mark enrollment as deleted
    data.is_deleted = True
    data.save()

    # Redirect to enrollment list
    return redirect('enrollment_list')


# Display all soft deleted enrollments
def restoreEnrollment(request):
    # Get all deleted enrollments
    enrollments = Enrollment.objects.filter(is_deleted=True)

    # Render restore enrollment page
    return render(request, 'restoreEnrollment.html', {'enrollments': enrollments})


# Restore a soft deleted enrollment
def restoreItem_enrollment(request, id):
    # Get enrollment by ID
    data = Enrollment.objects.get(id=id)

    # Restore enrollment
    data.is_deleted = False
    data.save()

    # Redirect to restore page
    return redirect('restoreEnrollment')


# Permanently delete a single enrollment
def delete_permanent(request, id):
    # Get enrollment by ID
    data = Enrollment.objects.get(id=id)

    # Permanently delete the enrollment
    data.delete()

    # Redirect to restore page
    return redirect('restoreEnrollment')


# Permanently delete all soft deleted enrollments
def delete_all(request):
    # Get all deleted enrollments
    data = Enrollment.objects.filter(is_deleted=True)

    # Permanently delete all deleted enrollments
    data.delete()

    # Redirect to restore page
    return redirect('restoreEnrollment')