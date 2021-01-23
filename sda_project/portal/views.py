from django.http import HttpResponse
from django.shortcuts import render

def downloads_view(request, *args, **kwargs):
    return render(request, "downloads.html", {})

def training_view(request, *args, **kwargs):
    return render(request, "training.html", {})