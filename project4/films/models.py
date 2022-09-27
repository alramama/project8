from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Film(models.Model):
    bid_description  = models.CharField(blank = True, max_length =255 )
    End_user = models.CharField(blank = True, max_length =255 )
    activity_type = models.CharField(blank = True, max_length =255 )
    reference_no = models.CharField(blank = True, max_length =50,primary_key=True )
    bid_info = models.FileField(upload_to='static',blank = True)
    bid_doc = models.FileField(upload_to='media',blank = True)


