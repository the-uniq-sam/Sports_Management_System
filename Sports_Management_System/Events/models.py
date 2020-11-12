from django.db import models
from django.forms import ModelForm

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=False)
    organiser = models.CharField(max_length=100)
    about = models.TextField(default='')
    rules = models.TextField(default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events'
