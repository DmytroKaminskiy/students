from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from students_app.models import Student


@receiver(pre_save, sender=Student)
def student_pre_save(sender, instance, **kwargs):
    print(instance.phone)
    instance.phone = ''.join(char for char in instance.phone if char.isdigit())
    # instance.save()  WRONG


@receiver(post_save, sender=Student)
def student_post_save(sender, instance, created, **kwargs):
    print('post_save\n' * 10)
    if created:
        pass
    # breakpoint()
