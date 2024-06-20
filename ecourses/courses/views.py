from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def index(request):
    return render(request, 'Hello')

def welcome(request, year):
    return HttpResponse("WELCOME" + str(year))
    
    
class TestView(View):
    
    def get(self, request):
        return HttpResponse("GET")
    
    def post(self, request):
        return HttpResponse("POST")
    