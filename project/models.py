from django.db import models
from core.models import NamedModel,Organization


class TaskCategoryModel(NamedModel):
    pass

class TaskModel(NamedModel):
    """ Model of something that can be done """
    category=models.ManyToManyField(
        TaskCategoryModel
    )

class Contribution(models.Model):
    task=models.ForeignKey(
        TaskModel,
        on_delete=models.PROTECT,
        help_text="What should be done."
    )

class ProjectModel(NamedModel):
    startDate=models.DateField(blank=True, null=True)
    endDate=models.DateField(blank=True, null=True)
    client=models.ForeignKey(Organization,on_delete=models.PROTECT,blank=True, null=True)
