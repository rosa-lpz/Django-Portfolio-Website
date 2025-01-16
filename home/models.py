from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


# Areas of Work / Services
class Areas_Work(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='home/images/')
    url = URLField(blank=True)

