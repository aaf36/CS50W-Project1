from django.shortcuts import render
from django.urls import reverse


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def entry(request, title):
    entries = util.list_entries()
    for entry in entries:
        if title.lower() == entry.lower():
            return render(request, "encyclopedia/entry.html", {
                "title":title,
                "title_content": util.get_entry(title),
            })
    return render(request, "encyclopedia/error404.html")

