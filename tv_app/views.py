from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    
    return render(request, "shows.html")

def shows(request):
    context = {
        "shows": Show.objects.all()
    }
    print(Show.objects.all())
    return render(request, "shows.html", context)

def addShow(request):
    
    return render(request, "addShow.html")

def processNew(request):
    errors = Show.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')


    this_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
    print(this_show)
    return redirect ('/shows')

def deleteShow(request, showId):
    show_to_delete = Show.objects.get(id=showId)
    show_to_delete.delete()

    return redirect ('/shows')

def showDisplay(request, showId):
    context = {
        "show": Show.objects.get(id=showId)
    }
    return render(request, "displayShow.html", context)
    
def showProcess(request, showId):
    this_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
    return redirect (f'/shows/{showId}')

def updateShow(request, showId):
    context = {
        "show": Show.objects.get(id=showId)
    }
    return render(request, "updateShow.html", context)


def updateNew(request, showId):

    this_show = Show.objects.get(id=showId)

    errors = Show.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/update/{showId}')

    show_to_update = Show.objects.get(id=showId)
    show_to_update.title = request.POST['title']
    show_to_update.network = request.POST['network']
    show_to_update.release_date = request.POST['release_date']
    show_to_update.desc = request.POST['desc']
    show_to_update.save()
    return redirect(f'/shows/{showId}')

