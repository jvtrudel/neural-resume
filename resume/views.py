from django.shortcuts import render, redirect
from resume.models import Resume
from resume.forms import ResumeForm
from django.http import Http404

#from resume.forms import ResumeForm

def list(request):
    """View of all available resumes"""
    resumes=Resume.objects.all()
    context={'list_object':resumes}
    return render(request,"resumes/list.html",context)

def show(request,id):
    """Non editable view of one resume"""
    resume=Resume.objects.get(id=id)
    form=ResumeForm(instance=resume)
    context={'resume': form, 'id':resume.id}
    return render(request,"resumes/show.html",context)

def create(request):
    """View to create a new resume"""
    resume=ResumeForm()
    print("create request method"+request.method)
    if request.method == "POST":
        resume=ResumeForm(request.POST)
        print("Form is valid? "+str(resume.is_valid()))
        if resume.is_valid():
            new_resume=resume.save()
            print("should redirect!")
            return redirect("resumes:show",id=new_resume.id)
    return render(request,"resumes/create.html", {'form':resume})

def update(request,id):
    """Editable view of a resume"""
    resume=Resume.objects.get(id=id)
    form=ResumeForm(instance=resume)
    context={'resume': form, 'id':resume.id}
    return render(request,"resumes/update.html",context)

def delete(request,id):
    """View to delete resume"""
    resume=Resume.objects.get(id=id)
    resume.delete()
    return redirect("resumes:list")

