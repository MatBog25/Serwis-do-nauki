from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name':'Python'},
    {'id':2, 'name':'Django'},
    {'id':3, 'name':'Frontend'},
]

def home(request):
    return render(request, 'home.html', {'rooms':rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    return render(request, 'room.html', {'room':room})