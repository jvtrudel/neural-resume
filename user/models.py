from django.db import models
from core.models import Person, Address, Job, Contribution, Quality, Skill, Interest

class User(Person):
    adresses=models.ManyToManyField(Address)
    jobs=models.ManyToManyField(Job,blank=True)
    contributions=models.ManyToManyField(Contribution,blank=True)
    qualities=models.ManyToManyField(Quality,blank=True)
    skills=models.ManyToManyField(Skill,blank=True)
    interets=models.ManyToManyField(Interest,blank=True)
