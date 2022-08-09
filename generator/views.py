from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def build_character_set():
    """ @brief Returns a list of characters acceptable for a password
    """
    characters = list(string.ascii_letters)
    characters.extend(string.punctuation)
    return characters


def home(request):
    # NOTE: This should return a properly formatted HTTP Response
    # or, of course, and object that spits such a thing.
    # return 'This should be an HTTP Response'
    return render(
            request,
            'generator/home.html',
            dict(password='orgohgoaj31234')
            )


def password(request):
    # NOTE: This should return a properly formatted HTTP Response
    # or, of course, and object that spits such a thing.
    # return 'This should be an HTTP Response'
    password_chars = build_character_set()
    length = int(request.POST['length'])
    proto_password = ''
    # password = ""
    for char in range(length):
        proto_password += random.choice(password_chars)


    return render(
            request,
            'generator/password.html',
            dict(password=proto_password)
            )
