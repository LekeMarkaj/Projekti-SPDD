from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

def about(request):
    return HttpResponse("Hello")


