from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):  
    name = models.CharField(max_length=100)
    native = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})

#Feeding Model
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Received food on on {self.date}"

    class Meta:
        ordering = ['-date']


    


