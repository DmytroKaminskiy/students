from django.contrib import admin
from django.conf import settings
from django.urls import include, path


from students_app.views import hello_world, students_list, create_student, edit_student, contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('students-list/', students_list, name='students-list'),
    path('create-student/', create_student),
    path('student-e/<int:primary_key>/', edit_student, name='student-edit'),
    path('contact-us/', contact_us, name='contact-us'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# client -> request -> wsgi server -> urls (path) -> hello_world(request) -> HttpResponse -> client
