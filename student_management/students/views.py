from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Display all active students and search students by name
@login_required(login_url='log_in')
def students_list(request):
    # Get search value from URL query (?searched=value)
    searched = request.GET.get('searched')

    # Method 1 (Alternative approach)
    # data = Student.objects.filter(is_delete=False)
    # if searched:
    #     data = Student.objects.filter(name__contains=searched)
    # else:
    #     data = Student.objects.all()

    # Method 2 (Current approach)
    if searched:
        # Show only active students whose name contains the search keyword
        data = Student.objects.filter(
            is_delete=False,
            name__contains=searched
        )
    else:
        # Show all active (non-deleted) students
        data = Student.objects.filter(is_delete=False)

    # Render student list page with student data
    return render(request, 'students/student_list.html', {'data': data})


# Display student form and save new student information
@login_required(login_url='log_in')
def students_form(request):
    # Check if form is submitted
    if request.method == 'POST' or request.FILES:
        # Get form data
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']
        dob = request.POST['dob']
        image = request.FILES.get('image')
        address = request.POST['address']

        # Create new student record
        Student.objects.create(
            name=name,
            number=phone,
            email=email,
            dob=dob,
            image=image,
            address=address
        )

        # Show success message
        messages.success(request, f'Hi {name} your form is submited')

        # Redirect back to the form page
        return redirect('form')

    # Display the student form page
    return render(request, 'students/students_form.html')


# Soft delete a student by setting is_delete=True
def delete_data(request, id):
    # Get student by ID
    data = Student.objects.get(id=id)

    # Mark student as deleted
    data.is_delete = True
    data.save()

    # Redirect to student list
    return redirect('list')


# Edit existing student information
def edit_data(request, id):
    # Get student details
    data = Student.objects.get(id=id)

    # Check if update form is submitted
    if request.method == 'POST' or request.FILES:
        data = Student.objects.get(id=id)

        # Update student information
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.number = request.POST['number']
        data.address = request.POST['address']
        data.dob = request.POST.get('dob')

        # Update image only if a new one is uploaded
        image = request.FILES.get('image')
        if image:
            data.image = image

        # Save updated record
        data.save()

        # Redirect to student list
        return redirect('list')

    # Display edit form with existing student data
    return render(request, 'students/edit.html', {'data': data})


# Display all soft deleted students
def restoreData(request):
    # Get all deleted students
    data = Student.objects.filter(is_delete=True)

    # Render restore page
    return render(request, 'students/restoreData.html', {'data': data})


# Restore a soft deleted student
def restoreItem_student(request, id):
    # Get student by ID
    data = Student.objects.get(id=id)

    # Restore student
    data.is_delete = False
    data.save()

    # Redirect to restore page
    return redirect('restoreData')


# Permanently delete a single student from the database
def delete_permanent(request, id):
    # Get student by ID
    data = Student.objects.get(id=id)

    # Permanently delete record
    data.delete()

    # Redirect to student list
    return redirect('list')


# Permanently delete all soft deleted students
def delete_all(request):
    # Get all deleted students
    data = Student.objects.filter(is_delete=True)

    # Permanently delete all records
    data.delete()

    # Redirect to restore page
    return redirect('restoreData')