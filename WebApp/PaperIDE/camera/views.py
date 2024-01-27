from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

def index(request):
    template = loader.get_template('camera.html')
    return HttpResponse(template.render())

def Home(request):
    return render(request, "")

# def camera(request):
#     template = loader.get_template('camera.html')
#     return HttpResponse(template.render())