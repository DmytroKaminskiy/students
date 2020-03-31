from django.http import HttpResponse
from students_app.models import Student


def hello_world(request):
    s = Student.objects.create(first_name='Dima', last_name='Kam', age=28, phone='123123123')
    return HttpResponse(s.first_name)
