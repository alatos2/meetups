from django.urls import path

from . import  views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), #your-domain.com/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), #your-domain.com/meetups/a-First-meetup
]
