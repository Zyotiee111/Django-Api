from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False, null= True , blank=True)

    def __str__(self):
        return self.title