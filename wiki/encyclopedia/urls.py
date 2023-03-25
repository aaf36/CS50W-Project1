from django.urls import path

from . import views


app_name ='wiki'

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_title>", views.entry_view, name="get_entry"),
    path("search", views.search, name="search")
]
