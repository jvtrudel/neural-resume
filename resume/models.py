from django.db import models
from core.models import Phone, Address, Fax


class Candidat(models.Model):
    firstName=models.CharField(
        max_length=50
    )
    lastName=models.CharField(
        max_length=50
    )
    email=models.EmailField()
    phone=Phone()

class Firm(models.Model):
    name=models.CharField(
        max_length=75
    )
    address=Address()
    fax=Fax()
    url=models.URLField()


class Resume(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    candidat=Candidat()
    firm=Firm()
