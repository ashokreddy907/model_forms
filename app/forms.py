from django import forms

from app.models import *

class SchoolModelForm(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'



class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'