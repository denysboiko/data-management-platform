from django.shortcuts import render
from .models import *


def main(request):
    return render(
        request,
        'index.html',
        {
            'items': Item.objects.all(),
            'user': request.user
        }
    )

def draggable(request):
    return render(
        request,
        'sidebar.html',
        {
            'user': request.user
        }
    )

def upload(request):
    return render(
        request,
        'upload.html',
        {
            'user': request.user
        }
    )