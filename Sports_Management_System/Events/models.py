from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=False)
    organiser = models.CharField(max_length=100)
    about = models.TextField(default='')
    rules = models.TextField(default='')
    temp = 'csvfile_for_guest/' + str(id) + '/'
    csvfile = models.FileField(upload_to=temp)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events'
