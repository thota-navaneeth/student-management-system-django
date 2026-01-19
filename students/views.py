from django.shortcuts import render, redirect
from .models import Student
from django.db import IntegrityError
# Create your views here.
def student_list(request):
    students = Student.objects.all()
    error = None

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        age = request.POST.get('age')

        try:
            Student.objects.create(
                name = name,
                email = email,
                course = course,
                age = age
            )
            return redirect('/')
        except IntegrityError:
            error = "Email already exists!"
            
    return render(request, 'students/students_list.html', {'students': students,'error':error})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def update_student(request,id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.age = request.POST.get('age')
        student.save()
        return redirect('/')
    return render(request, 'students/update_student.html',{'student': student})