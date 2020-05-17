from time import sleep

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def django_sleep(student_id):
    from students_app.models import Student

    student = Student.objects.get(id=student_id)
    print('START')
    sleep(student.age or 10)
    print('END')


@shared_task
def beat():
    print('beat START')
    sleep(5)
    print('beat END')


@shared_task(autoretry_for=(ConnectionError, ), default_retry_delay=60, max_retries=3)
def send_email_async(data):
    send_mail(
        data['subject'],
        data['message'],
        data['email'],
        [settings.EMAIL_HOST_USER],
        # ['fenderoksp@gmail.com'],
        fail_silently=False,
    )
