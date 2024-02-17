from django.shortcuts import render

# Create your views here.1

rooms =[
    {'id':1, 'name':' Let us learn python!'},
    {'id':2, 'name':' Design with me'},
    {'id':3, 'name':' Let us learn Django!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id']==int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)