from django.urls import path
from .  import views 

urlpatterns = [
    
  
    path("", views.index, name='index'),
    path("students/<int:student_id>/",views.details, name = 'details'),
    path("add_student", views.add_student, name="add_student"),
    path('courses/', views.courses, name='courses'),
    path('add_course/', views.add_course, name='add_course'),
    
hit c