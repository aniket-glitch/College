from django.shortcuts import render
from .tables import *
from .models import *

available_model = {
    "teacher": [Teacher, TeacherTable, TeacherFilter],
    "subject": [Subject, SubjectTable,None],
    "class": [Class, ClassTable, None],
    "student": [Student, StudentTable,None],

}


def home(request):
    table = AvailableTable([{"model": i} for i in available_model.keys()])

    return render(request, "table.html", {
        "table": table,
        "model_name": "Models"
    })


def models(request, model_name):
    if available_model.get(model_name):
        model, model_table,filter_object = available_model.get(model_name)
        # table = model_table(model.objects.all())
        model_data = model.objects.all()
        if filter_object:
            query = request.GET.copy()

            if len(query) == 0:
                query['jobnumber'] = 0

            user_filter = filter_object(query, queryset=model_data)
            table = model_table(user_filter.qs)
        else:
            user_filter = None
            table = model_table(model_data)
        return render(request, "table.html", {
            "table": table,
            "model_name": model.__name__,
            "filter": user_filter
        })
