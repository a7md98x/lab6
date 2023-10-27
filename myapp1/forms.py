from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'
    

class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'
