from django.db import models
from datetime import *

# Create your models here.
class Blog(models.Model):

    datepub = models.DateTimeField(default=datetime.now())
    title = models.TextField('Title')
    text = models.TextField('Text')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"



