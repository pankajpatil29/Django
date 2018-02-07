# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models

class Create(models.Model):
    EmpId = models.AutoField(primary_key=True)
    EmpName  = models.CharField(max_length=45)
    Address = models.CharField(max_length=45)
    EmailId = models.EmailField(unique=True, max_length=45)
    Password = models.CharField(max_length=300)
    Phone = models.CharField(max_length=45)
    AccessToken = models.CharField(max_length=50)
    Image = models.ImageField(default = 'pic_folder/None/no-img.jpg')


    class Meta:
        managed = False
        db_table = 'Details'


# Create your models here.
