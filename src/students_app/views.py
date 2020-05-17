from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from students_app.tasks import django_sleep

from students_app.models import Student, Group


def hello_world(request):
    print('hello_world')
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

def create_student(request):
    from students_app.forms import StudentForm
    from django.urls import reverse
    form_class = StudentForm


    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students-list'))
    elif request.method == 'GET':
        form = form_class(initial={'age': 16})

    return render(request, 'create-student.html', {'create_form': form, 'one': 1})


def edit_student(request, primary_key):
    from students_app.forms import StudentForm
    from students_app.models import Student
    from django.http import Http404

    form_class = StudentForm

    try:
        student = Student.objects.get(id=primary_key)
    except Student.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = form_class(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students-list'))
    elif request.method == 'GET':
        form = form_class(instance=student)

    return render(request, 'edit-student.html', {'form': form})


def contact_us(request):
    from students_app.forms import ContactUs
    from django.urls import reverse
    form_class = ContactUs

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students-list'))
    elif request.method == 'GET':
        form = form_class()

    return render(request, 'contact-us.html', {'form': form})


def group_list(request):
    groups = Group.objects.all().select_related('head')
    return render(request, 'group-list.html', {'objects_list': groups})

# -------request-----view------sleep(5)!!!!! ------ response

# -------request-----view------ sleep(5).send() ------ response
# -----------------------------sleep(5)------------------------


def slow_view(request):
    student = Student.objects.last()
    # django_sleep.delay(student.id)  # django_sleep(num) str, int, list, dict
    django_sleep.apply_async(args=[student.id], countdown=10)  #  django_sleep.apply_async(kwargs={'student_id': student.id})
    return HttpResponse('SLOW')


'''
GET
http://127.0.0.1:8000/create-student/?first_name=&age=22&phone=awdawawdaw

POST
head
http://127.0.0.1:8000/create-student/

body
first_name=&age=22&phone=awdawawdaw

1xx - INFO 
2xx - OK, 200
3xx - Redirect 302
4xx - client error 404 (not found), 400 - Bad request, 401 - Not authorized
5xx - server error, 500 (server error), 503
'''
