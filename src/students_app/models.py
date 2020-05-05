from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from students.tasks import django_sleep

# pk - primary key
class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField(null=True, default=None, validators=[MinValueValidator(10), MaxValueValidator(100)])
    phone = models.CharField(max_length=20, default='')  # RegexValidator

    def info(self):
        return f'{self.id} ${self.first_name} ${self.last_name} ${self.age} {self.phone}'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Group(models.Model):
    name = models.CharField(max_length=64)
    # head = models.OneToOneField()
    # head = models.ForeignKey(Student, on_delete=models.CASCADE)
    head = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='groups')  # head_id
    # head = models.ForeignKey('students_app.Student', on_delete=models.SET_NULL, null=True)


'''
client -> ||| server -> DB -> server ||| -> client
'''

'''
User - Subscription
User - Order
Teacher - Group

Teacher - id [1, 2, 3]
teacher_group [id, teacher_id, group_id]
Group - id [2, 3, 4]


(1, 1, 2)
(2, 1, 4)
(3, 2, 4)
'''
