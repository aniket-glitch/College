from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Class)
admin.site.register(ClassStudent)
admin.site.register(Student)
admin.site.register(StudentContact)
