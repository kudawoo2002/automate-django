from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")


def importdata(request):
    return render(request, "dataentry/importdata.html")