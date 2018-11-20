from django.db import models

from markupfield.fields import MarkupField


# Create your models here.


class Inspection(models.Model):
    address = models.TextField()
    description = MarkupField(markup_type='markdown')
    plumbing = models.BooleanField(default=False)
    electrical = models.BooleanField(default=False)
    roofing = models.BooleanField(default=False)
    mold = models.BooleanField(default=False)
    termites = models.BooleanField(default=False)
    basement = models.BooleanField(default=False)
    chimney = models.BooleanField(default=False)
    gutters = models.BooleanField(default=False)
    radon = models.BooleanField(default=False)

    photo = models.ImageField(upload_to='inspection_photo')
    inspection_file = models.FileField(upload_to='inspections')

    def __str__(self):
        return self.address
