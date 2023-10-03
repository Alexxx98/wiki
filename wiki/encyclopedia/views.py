from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import NewPage

from . import util

import markdown as md

import random


def index(request):
    if request.method == "POST":
        query = request.POST['q']
        return HttpResponseRedirect(f"{query}")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def entry(request, title):
    request.session['entries'] = []
    if request.method == "POST":
        query = request.POST['q']
        return HttpResponseRedirect(f"{query}")

    for entry in util.list_entries():
        if title.lower() == entry.lower():
            title = entry
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": md.markdown(util.get_entry(title), extensions=['fenced_code']),
            })
        elif title.lower() in entry.lower():
            request.session['entries'] += [entry]

    return render(request, "encyclopedia/search.html", {
        "entries": request.session['entries'],
    })

def new_page(request):
    entries = util.list_entries()
    if request.method == "POST":
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            if title not in entries:
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "encyclopedia/page_exists.html", {
                    "title": title
                })

    return render(request, "encyclopedia/new_page.html", {
        "form": NewPage()
    })

def edit(request, title):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "encyclopedia/edit.html", {
        "title": title, "content": util.get_entry(title)
    })

def random_page(request):
    entries = util.list_entries()
    title = random.randint(0, len(entries) - 1)
    return HttpResponseRedirect(f"{entries[title]}")


