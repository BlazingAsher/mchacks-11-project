from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. This will become a camera eventually.")

def Home(request):
    return render(request, "")