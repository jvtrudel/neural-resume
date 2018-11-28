from django.db import models

STATUS=(
  ('C','Current'),
  ('F','Finished'),
  ('A', 'Active'),
  ('S','Stopped')
)


class NamedModel(models.Model):
  """ Model of something that have a name and a description """
  name=models.CharField(
    max_length=50,
    help_text="A brief, memorable and descriptive name",
    unique=True,
    default="Object Name"
  )
  brief=models.TextField(
    max_length=250,
    help_text="A short description of the task",
    null=True,blank=True
  )
  def __str__(self):
    return "{}".format(self.name)

class Person(models.Model):
  firstName=models.CharField(
    max_length=50,
    help_text="First Name"
  )
  lastName=models.CharField(
    max_length=50,
    help_text="Last Name"
  )
  birthDate=models.DateField()
  def __str__(self):
    return "{} {}".format(self.firstName, self.lastName)

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

class PhoneNumber(models.Model):
  number=models.CharField(max_length=50)
  def __str__(self):
    return self.number

class Location(NamedModel):
  address=models.ForeignKey(Address,on_delete=models.PROTECT)
  phone=models.ManyToManyField(PhoneNumber)


class Organization(NamedModel):
  locations=models.ManyToManyField(Location)

class Category(NamedModel):
    isA=models.ManyToManyField("self",blank=True)
    hasA=models.ManyToManyField("self",blank=True)

class Skill(NamedModel):
    isA=models.ManyToManyField("self",blank=True)
    hasA=models.ManyToManyField("self",blank=True)

class Quality(NamedModel):
    isA=models.ManyToManyField("self",blank=True)
    hasA=models.ManyToManyField("self",blank=True)

class Interest(NamedModel):
    isA=models.ManyToManyField("self",blank=True)
    hasA=models.ManyToManyField("self",blank=True)

class JobDescription(NamedModel):
  needed_skils=models.ManyToManyField(Skill,help_text="Des compétences nécessaires",blank=True)
  needed_quality=models.ManyToManyField(Quality,help_text="Des qualités requises ou qui aident à bien faire le travail",blank=True)
  needed_interest=models.ManyToManyField(Interest, help_text="Des intérêts pour certaines choses",blank=True)

class Job(models.Model):
  JOB_TYPE=(
    ('E','Employee'),
    ('F','Freelance'),
    ('C','Contractual'),
    ('EN','Entrepreneur'),
    ('T','Trainee'),
    ('V','Volunteer'),
     ('H','Hobbyist'),
     ('O','Other')
  )
  JOB_STATUS=(
    ('C','Current'),
    ('F','Finished')
  )
  description=models.ForeignKey(JobDescription,on_delete=models.PROTECT)
  status=models.CharField(max_length=20,choices=JOB_STATUS, blank=True, null=True)
  jobType=models.CharField(max_length=20,choices=JOB_TYPE, blank=True, null=True)
  organization=models.ManyToManyField(Organization)
  startDate=models.DateField(blank=True, null=True)
  endDate=models.DateField(blank=True, null=True)



class Diplome(models.Model):
  title=models.CharField(max_length=50)
  grade=models.CharField(max_length=50)
  specialization=models.CharField(max_length=150,blank=True,null=True)
  description=models.TextField(blank=True,null=True)
  def __str__(self):
    return self.title


class Scholarite(models.Model):
  diplome=models.ForeignKey(Diplome, on_delete=models.PROTECT)
  startDate=models.DateField(blank=True,null=True)
  endDate=models.DateField(blank=True,null=True)
  institutions=models.ManyToManyField(Organization)
  status=models.CharField(max_length=20,choices=STATUS, blank=True, null=True,default='F')
  def __str__(self):
    out=self.diplome.__str__()+"\n"
    n=len(institutions.all())
    i=1
    for school in institutions.all():
      out+=school.__str__()
      if n!=i:
        out+=", "
      i+=1
    return out

class Formation(NamedModel):
  diplome=models.ForeignKey(Diplome, on_delete=models.PROTECT,blank=True,null=True)
  startDate=models.DateField(blank=True,null=True)
  endDate=models.DateField(blank=True,null=True)
  institution=models.ForeignKey(Organization,on_delete=models.PROTECT)
  status=models.CharField(max_length=20,choices=STATUS, blank=True, null=True,default='F')

class Task(NamedModel):
    """ Model of something that can be done """
    category=models.ManyToManyField(
        Category
    )

class Contribution(NamedModel):
    activity=models.ForeignKey(
        Task,
        on_delete=models.PROTECT,
        help_text="What should be done."
    )
    nuberOfHours=models.FloatField()
    startDate=models.DateField(blank=True,null=True)
    endDate=models.DateField(blank=True,null=True)


class WebTool(NamedModel):
  pass

class WebToolInstance(models.Model):
  owner=models.ForeignKey(Organization,on_delete=models.PROTECT)
  tool=models.ForeignKey(WebTool,on_delete=models.PROTECT)
  url=models.URLField()

