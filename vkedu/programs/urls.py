from django.contrib import admin
from django.urls import path, re_path

import programs.views as vw

urlpatterns = [
    path('', vw.prog_name),
    re_path('([0-9]+)', vw.prog_name),
]
