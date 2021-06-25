from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup

# Create your views here.

def index(request):
    # return HttpResponse('hello world!!!')
    # meetups = [
    #     {'title': 'This is my first meetup', 'location': 'Nigeria', 'slug': 'a-first-meetup' },
    #     {'title': 'This is my second meetup', 'location': 'America', 'slug': 'a-second-meetup' }
    # ]
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    # selected_meetup = {'title': 'A First Meetup', 'description': 'This is the first meetup!' }
    try:
        selected_meetup = Meetup.objects.get(slug = meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
