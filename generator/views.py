from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # NOTE: This should return a properly formatted HTTP Response
    # or, of course, and object that spits such a thing.
    # return 'This should be an HTTP Response'
    return HttpResponse('<h1>This should be an HTTP Response</h1>')
