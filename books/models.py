from django.db import models
import datetime
from django.contrib.auth.models import User


class books (models.Model):
    title = models.CharField(max_length = 50)
    publication_date = models.DateField()

    def __str__(self):
        return "%s" % (self.title)

class comments (models.Model):
    id_book = models.ForeignKey (books, null = True, blank = True, on_delete = models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateField(default = datetime.date.today)
    id_user = models.ForeignKey (User, null = True, blank = True, on_delete = models.CASCADE)
    
    def __str__(self):
        return "%s" % (self.text)









