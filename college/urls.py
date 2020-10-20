from django.urls import path
from . import views
from django import urls

urlpatterns = [
    # ex: /polls/
    # path('teachers/', views.teacher_list),
    path('', views.home),
    path('model/<str:model_name>', views.models),
]