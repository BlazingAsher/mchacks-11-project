from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from django.views.decorators.csrf import csrf_exempt

from .image_processing_worker import submit_image
from .services.speech_recognition import update_image

import json

def index(request):
    template = loader.get_template('camera.html')
    return HttpResponse(template.render())

# To request an image to be processed, send a POST request to
# /camera/submitImage with a JSON body like so:
# { "imageData": "<base64 encoded string of the image>" }
@csrf_exempt
def submitImage(request):
    try:
        req_obj = json.loads(request.body)
        # submit an image to the processing queue, so that request doesn't take forever
        update_image(req_obj["imageData"])
        return HttpResponse("OK")
    except json.JSONDecodeError:
        return HttpResponse("Bad JSON!")

def Home(request):
    return render(request, "")

# def camera(request):
#     template = loader.get_template('camera.html')
#     return HttpResponse(template.render())