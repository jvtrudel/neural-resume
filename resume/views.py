from django.shortcuts import render, redirect
from resume.models import Resume

#from resume.forms import ResumeForm

def list(request):
    """View of all available resumes"""
    resumes=Resume.objects.all()
    context={'list_object':resumes}
    return render(request,"resumes/list.html",context)

def show(request,id):
    """View of all one resume"""
    return render(request,"resumes/show.html")

def create(request):
    """View to create a new resume"""
    return render(request,"resumes/create.html")

def update(request,id):
    """View to edit a resume"""
    return render(request,"resumes/update.html")

def delete(request,id):
    """View to delete resume"""
    return redirect("resumes:list")
