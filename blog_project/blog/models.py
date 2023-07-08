from django.db import models

class contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    desc= models.CharField(max_length=1000)
    date= models.DateField()

    def __dtr__(self):
        return self.name