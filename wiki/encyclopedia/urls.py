from django.urls import path

from . import views


app_name ='wiki'

urlpatterns = [
    path("", views.index, name="index"),
    path("get/<str:entry_title>", views.entry_view, name="get_entry"),
    path("search/", views.search, name="search"),
    path("create/", views.newEntry_view, name="new"),
    path("edit/", views.editEntry, name="edit"),
    path("save/", views.save, name="save")
]
