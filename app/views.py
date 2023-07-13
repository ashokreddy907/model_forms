from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_school(request):
    SMFO=SchoolModelForm
    d={'SMFO':SMFO}
    if request.method=='POST':
        SMFOD=SchoolModelForm(request.POST)
        if SMFOD.is_valid():
            SMFOD.save()
        return HttpResponse('Data is Successfully Inserted')
    return render(request,'insert_school.html',d)


def insert_student(request):
    SMF=StudentModelForm
    d={'SMF':SMF}
    if request.method=='POST':
        SMFD=StudentModelForm(request.POST)
        if SMFD.is_valid():
            SMFD.save()
        return HttpResponse('Data Is Successfully Inserted')
    return render(request,'insert_student.html',d)
