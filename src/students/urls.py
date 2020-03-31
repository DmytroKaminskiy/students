from django.contrib import admin
from django.urls import path

from students_app.views import hello_world


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
]

# client -> request -> wsgi server -> urls (path) -> hello_world(request) -> HttpResponse -> client
