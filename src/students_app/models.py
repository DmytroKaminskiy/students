from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField(null=True, default=None)
    phone = models.CharField(max_length=20, default='')

    def info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.phone}'

# create table first_name Varchar(128)
