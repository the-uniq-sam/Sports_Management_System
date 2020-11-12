from django.db import models
from django.forms import ModelForm

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=False)
<<<<<<< HEAD
    organiser = models.CharField(max_length=100)
    about = models.TextField(default='')
    rules = models.TextField(default='')

=======
    organiser = models.CharField(max_length=200)
    temp = 'csvfile_for_guest/' + str(id) + '/'
    csvfile = models.FileField(upload_to=temp)
>>>>>>> 8f17f98558999da507d00cb803902379e80b64c7

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events'
