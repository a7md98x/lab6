from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.

def index (request):
    s1 = students.objects.all()
    student_form = StudentForm() 

    return render(request,"myapp1/index.html",{
          "students_list" : s1,"student_form": student_form})
    
def student (request, students_id):
    s = students.objects.all()
    student_form = StudentForm()
    return render(request, "myapp1/student.html",
          {"s": s}        
    )
def add_student(request):
    student_form = StudentForm()
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            student_form = StudentForm() # reset form after submiting
    students_list = students.objects.all()
    return render(request, 'myapp1/index.html', {'students_list': students_list, 'student_form': student_form})

    
    

def courses(request):
    courses_list = course.objects.all()
    course_form = CourseForm()
    return render(request, 'myapp1/course.html', {'courses_list': courses_list, 'course_form': course_form})

def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            course_form = CourseForm() # reset form  after submiting
    else:
          course_form = CourseForm()     
    courses_list = course.objects.all()
    return render(request, 'myapp1/course.html', {'courses_list': courses_list, 'course_form': course_form})


def details(request, student_id):
    student = students.objects.get(pk=student_id)
    students_list = students.objects.all()

    available_courses = course.objects.exclude(students=student)
    
    if request.method == 'POST':
        course_id = request.POST['course']
        course_to_add = course.objects.get(pk=course_id)
        student.courses.add(course_to_add)
        return HttpResponseRedirect(reverse('details', args=[student_id]))
    
    
    return render(request, 'myapp1/details.html', {'student': student, 'students_list': students_list, 'available_courses': available_courses})
