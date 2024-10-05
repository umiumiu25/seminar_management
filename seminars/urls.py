# seminars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.seminar_list, name="seminar_list"),
    path("<str:pk>/", views.seminar_detail, name="seminar_detail"),
    path("<str:pk>/apply/", views.apply_seminar, name="apply_seminar"),
]
