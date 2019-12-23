from django.contrib.auth.models import User
from django.db import models


# Database created for PDF file
class pdf_file(models.Model):
    name = models.CharField(max_length=100)
    pdffile = models.FileField()

    def __str__(self):
        return self.name