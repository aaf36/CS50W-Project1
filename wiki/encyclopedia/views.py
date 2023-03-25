from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2   # ignore


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def convert_markdown_to_Html(markdownText):
    HtmlText =markdown2.markdown(markdownText)
    return HtmlText


def entry_view(request, entry_title):
    entries= util.list_entries()
    for entry in entries:
        if entry_title.lower()== entry.lower():
            text =util.get_entry(entry_title)
            entry_content= convert_markdown_to_Html(text)
            return render(request, "encyclopedia/entry.html", {
                    "entry_title":entry_title,
                    "entry_content":entry_content
                })
    return render(request, "encyclopedia/error404.html")
   
    

         

def search(request):
    matched_queries=[]
    if request.method =='GET':
        query =request.GET.get('q')
        Squery =str(query)
        entiries =util.list_entries()
        for entry in entiries:
            if Squery.lower()==entry.lower():
                query_text= util.get_entry(query)
                query_content = convert_markdown_to_Html(query_text)
                return render(request, "encyclopedia/entry.html", {
                    "entry_title": query,
                    "entry_content": query_content
                })
            elif Squery.lower() in entry.lower():
                matched_queries.append(entry)
                return render(request, "encyclopedia/search_result.html", {
                "results":matched_queries
                })
                
        





