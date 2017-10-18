from django.shortcuts import render
from django.http import HttpResponse
import requests
import base64

# Create your views here.
def index(request):
    page = requests.get("http://127.0.0.1:8080/")
    response = page.json()
    encoded_image_data = response['encoded_image_data']
    image_data = base64.b64decode(encoded_image_data)
    return HttpResponse(image_data, content_type='image/png')