from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('hello world!!!')
    meetups = [
        {'title': 'This is my first meetup'},
        {'title': 'This is my second meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
