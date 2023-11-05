from django.urls import path, re_path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard),
    path("profile/", views.profile),
    path("form/", views.form_submit),
]
