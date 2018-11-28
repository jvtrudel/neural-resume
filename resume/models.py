from django.db import models
from user.models import User
from core.models import NamedModel, Scholarite, Formation, Organization



class Biography(models.Model):
    brief=models.CharField(max_length=500,blank=True,null=True)
    full=models.TextField(blank=True,null=True)


class Resume(NamedModel):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    firm=models.ForeignKey(Organization,on_delete=models.PROTECT)
    bio=Biography()
    scholarite=models.ManyToManyField(Scholarite)
    perfectionnement=models.ManyToManyField(Formation)

    
