from django.db import models

class Phone(models.Model):
    number=models.CharField(max_length=20)
    extension=models.CharField(max_length=20,blank=True,null=True)

class Fax(models.Model):
    number=models.CharField(max_length=20)

class Address(models.Model):
  civicNumber=models.IntegerField()
  streetType=models.CharField(max_length=50)
  streetName=models.CharField(max_length=50)
  officeNumber=models.CharField(max_length=12,blank=True,null=True)
  postalCode=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  state=models.CharField(max_length=50,blank=True,null=True)
  country=models.CharField(max_length=50)
  def __str__(self):
    outString="{} {} {} ".format(self.civicNumber, self.streetType,self.streetName)
    if self.officeNumber:
      outString+="\nBureau {}".format(self.officeNumber)
    outString+="\n{} \n{}".format(self.postalCode,self.city)
    if self.state:
      outString+="\n{}".format(self.state)
    outString+="\n{}".format(self.country)
    return outString
