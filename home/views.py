from django.shortcuts import render


def index(req):
    return render(req, 'home/index.html'),

# Create your views here.
