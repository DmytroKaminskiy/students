from django.core.management.base import BaseCommand
from students_app.models import Student


class Command(BaseCommand):
    help = 'Clean students phone!!!'

    def handle(self, *args, **options):
        # 100,000,000
        for student in Student.objects.exclude(phone='').iterator():
            # 1
            # phone = ''
            # for char in student.phone:
            #     if char.isdigit():
            #         phone += char
            ##########################
            # phone = ''.join([char for char in student.phone if char.isdigit()])
            phone = ''.join(char for char in student.phone if char.isdigit())
            # phone = ''.join(filter(lambda x: x.isdigit(), student.phone))
            student.phone = phone
            student.save()


# [i for i in range(10)]
# (i for i in range(10))
