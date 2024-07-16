from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Python'},
#     {'id':2, 'name':'Django'},
#     {'id':3, 'name':'Frontend'},
# ]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms':rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)

    return render(request, 'room.html', {'room':room})

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'room_form.html', {'form':form})

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'room_form.html', {'form':form})

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)  
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'delete.html', {'obj':room})