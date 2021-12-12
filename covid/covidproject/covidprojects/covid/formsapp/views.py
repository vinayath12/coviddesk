from django.contrib import messages
from django.shortcuts import render, redirect
from .models import forms
# Create your views here.
def createform(request):
    try:
     if request.method=='POST':
        name=request.POST.get('name',)
        gender = request.POST.get('gender',)
        age = request.POST.get('age',)
        email = request.POST.get('email',)
        dob = request.POST.get('dob',)
        number = request.POST.get('number',)
        place = request.POST.get('place',)
        job = request.POST.get('job',)
        vaccines = request.POST.get('vaccines',)
        traveling = request.POST.get('traveling',)
        covidecheck = request.POST.get('covidecheck',)
        form=forms(name=name,Gender=gender,age=age,email=email,dob=dob,number=number,place=place,job=job,vaccines=vaccines,traveling=traveling,covidecheck=covidecheck)
        form.save()
        return redirect('success')
     return render(request, 'forms.html')
    except:
        messages.info(request, "you have to fill all the field,fill again")
        return redirect('createform')
        # messages.info(request,"fill all fields")
   # return render(request,'forms.html')
def success(request):
    return render(request,'redirect.html')