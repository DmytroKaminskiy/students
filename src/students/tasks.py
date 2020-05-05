from time import sleep

from celery import shared_task


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
