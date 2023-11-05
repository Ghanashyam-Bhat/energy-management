from django.urls import path, re_path
from . import views

urlpatterns = [
    path("profile/", views.profile),
    path("form/", views.form_submit),
]
