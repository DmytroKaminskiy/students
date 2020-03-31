from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField(null=True, default=None)
    phone = models.CharField(max_length=20, default='')

# create table first_name Varchar(128)
