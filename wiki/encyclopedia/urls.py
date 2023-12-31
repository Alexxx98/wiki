from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new_page, name="new_page"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.random_page, name="random"),
    path("<str:title>", views.entry, name="entry"),
]

