from django.shortcuts import render
from resume.models import Resume


def list(request):
    resumes=Resumes.objects,all()
    return render(request, 'resume/list.html',{'resumes': resumes})
