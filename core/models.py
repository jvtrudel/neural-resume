from django.db import models

# Create your models here.

class Person(models.Model):
  firstName=models.CharField(max_length=50)
  lastName=models.CharField(max_length=50)
  birthDate=models.DateField()

class Address(models.Model):
  civicNumber=models.IntegerField()
  streetName=models.CharField(max_length=50)
  streetType=models.CharField(max_length=50)
  postalCode=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  state=models.CharField(max_length=50)
  country=models.CharField(max_length=50)

class PhoneNumber(models.Model):
  number=models.CharField(max_length=50)

class Organization(models.Model):
  name=models.CharField(max_length=50)
  address=models.ForeignKey(Address,on_delete=models.DO_NOTHING)



