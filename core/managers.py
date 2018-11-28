from django.db import models
from treelib import Node, Tree

class AttributTreeManager(models.Manager):
    def get_queryset(self):
        pass
