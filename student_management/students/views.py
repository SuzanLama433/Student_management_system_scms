from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

def students_list(request):
    data = Student.objects.filter(is_delete=False)
    return render(request,'students/student_list.html' ,{'data' : data})

def students_form(request):
    if request.method == 'POST' or request.FILES:
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']
        dob = request.POST['dob']
        image = request.FILES.get('image')    
        address = request.POST['address']
        Student.objects.create(name=name,number=phone,email=email,dob=dob,image=image,address=address)
        
        messages.success(request,f'Hi {name} your form is submited')
        return redirect('form')
            
        
    return render (request,'students/students_form.html')

def delete_data (request,id):
    data = Student.objects.get(id=id)
    data.is_delete = True
    data.save()
    return redirect('list')

def edit_data(request,id):
    data = Student.objects.get(id=id)
    if request.method == 'POST' or request.FILES:
        data = Student.objects.get(id=id)
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.number= request.POST['number']
        data.address = request.POST['address']
        dob = request.POST['dob']
        image = request.FILES.get('image')
        if image:
            data.image = image
        elif dob:
            data.dob = dob
        data.save()
        return redirect('list')
    return render(request,'students/edit.html',{'data':data})

def restoreData(request):
    data = Student.objects.filter(is_delete=True)
    return render(request,'students/restoreData.html',{'data':data})

def restoreItem_student(request,id):
    data = Student.objects.get(id=id)
    data.is_delete = False
    data.save()
    return redirect('restoreData')  
   
def delete_permanent(request,id):
    data = Student.objects.get(id = id)
    data.delete()
    return redirect('list')

def delete_all(request):

    data = Student.objects.filter(is_delete = True)
    data.delete() #permanent delete
    return redirect('restoreData')