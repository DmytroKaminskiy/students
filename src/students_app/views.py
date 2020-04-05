from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from students_app.models import Student


def hello_world(request):
    s = Student.objects.create(first_name='Dima', last_name='Kam', age=28, phone='123123123')
    return render(request, 'hello.html')


def students_list(request):
    students = Student.objects.all()
    # print(students.query)

    age_to_filter = request.GET.get('age')
    if age_to_filter:
        students = students.filter(age__lte=age_to_filter)  # WHERE
        # students = students.filter(age__gt=age_to_filter)  # WHERE "students_app_student"."age" > 40 gt, gte, lt, lte
        # students = students.filter(age__startswith=age_to_filter)  # "students_app_student"."age" LIKE 2% ESCAPE '\'
        # students = students.filter(age__endswith=age_to_filter)  # "students_app_student"."age" LIKE %2 ESCAPE '\'
        # students = students.filter(age__endswith=age_to_filter, age__startswith=age_to_filter)
        # students = students.exclude(age=age_to_filter)
        # students = students.filter(~Q(age=age_to_filter))
        # WHERE NOT ("students_app_student"."age" = 40 AND "students_app_student"."age" IS NOT NULL)

    # first_name = request.GET.get('fn')
    # if first_name:
    #     # q = Q(first_name__startswith='a') | Q(last_name__endswith='a')
    #     q = ~Q(first_name__startswith='a')
    #     q |= Q(last_name__endswith='a')
    #     # (NOT ("students_app_student"."first_name" LIKE a% ESCAPE '\') OR "students_app_student"."last_name" LIKE %a ESCAPE '\')
    #     students = students.filter(q)

    #/ ?age = 40 & order - by = first_name,-last_name
    # print(students.count())
    sorting = request.GET.get('order-by')
    if sorting:
        students = students.order_by(*sorting.split(','))
    # students = students.order_by('first_name', '-last_name')
    # students.delete()

    print(students.query)
    return render(request, 'students-list.html', {'students': students})

# MVC
# M - model
# V - view - html
# C -controller - django view

# MTV
# M - model
# T - template  (V)
# U - URLS
# V - view (C)


# MTR
# m -model
# t - template
# r -resource
