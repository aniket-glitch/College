import django_tables2 as tables
from .models import *
from django.utils.safestring import mark_safe
import django_filters


class AvailableTable(tables.Table):
    model = tables.Column()

    class Meta:
        template_name = "django_tables2/bootstrap.html"

    def render_model(self, value):
        return mark_safe("<a href=\"/model/{name}\"> {name} </a>".format(name=value))


class TeacherTable(tables.Table):
    subjects = tables.Column()

    class Meta:
        template_name = "django_tables2/bootstrap.html"
        model = Teacher

    def render_subjects(self, record):
        return ",".join([i.name for i in record.subjects.all()])


class TeacherFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='doj', lookup_expr=('lt'))
    end_date = django_filters.DateFilter(field_name='doj', lookup_expr=('gt'))

    class Meta:
        model = Teacher
        fields = ['id']


class SubjectTable(tables.Table):
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        model = Subject


class StudentTable(tables.Table):
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        model = Student


class ClassTable(tables.Table):
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        model = Class
