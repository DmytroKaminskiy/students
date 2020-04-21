from django.contrib import admin

from students_app.forms import StudentForm
from students_app.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'phone')
    # readonly_fields = ('age', )
    # search_fields = ('=first_name', '=last_name')
    search_fields = ('first_name', 'last_name')
    form = StudentForm
    ordering = ('age', )


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'head')
    list_select_related = ['head']  # Group.objects.all() -> Group.objects.all().select_related('head')
    list_per_page = 10


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
