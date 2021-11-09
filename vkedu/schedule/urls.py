from django.urls import path, include, re_path
from schedule.views import all_lesson_name, lesson_name

urlpatterns = [
    path('', all_lesson_name),
    re_path('([0-9]+)', lesson_name),
]
