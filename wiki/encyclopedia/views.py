from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2   # ignore


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def entry_view(request, entry_title):
    entries= util.list_entries()
    for entry in entries:
        if entry_title.lower()== entry.lower():
            text =util.get_entry(entry_title)
            entry_content= markdown2.markdown(text)
            return render(request, "encyclopedia/entry.html", {
                    "entry_title":entry_title,
                    "entry_content":entry_content
                })
            
    return render(request, "encyclopedia/error404.html", status=404)
    
    
         

def search(request):
    entries = util.list_entries()
    query = request.GET['q']
    for entry in entries:
            if query.lower() == entry.lower():
                return redirect("wiki:get_entry", entry=query)
                
        




