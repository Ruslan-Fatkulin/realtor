from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


def home(request):
    houses = House.objects.all().order_by('-date_added')
    return render(request, 'home.html', {'houses': houses})


@login_required(login_url='/auth/login/')
def create(request):
    form = BaseForm(request.POST, request.FILES)
    image_form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            dom = House.objects.create(seller=request.user, **form.cleaned_data)
            if image_form.is_valid():
                a = image_form.save(commit=False)
                a.house = dom
                a.save()
        if dom.type == 'квартира':
            return redirect('house:create_apartment', dom.pk)
        if dom.type == 'дом':
            return redirect('house:create_house', dom.pk)
    return render(request, 'create.html', {'form': form, 'form2': image_form})


def create_apartment(request, pk):
    house = House.objects.get(pk=pk)
    form = ApartamentForm(request.POST, instance=house)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('house:home')
    return render(request, 'create_apartament.html', {'form': form})


def create_house(request, pk):
    house = House.objects.get(pk=pk)
    form = HouseForm(request.POST, instance=house)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('house:home')
    return render(request, 'create_house.html', {'form': form})


def detail(request, pk):
    house = House.objects.get(pk=pk)
    images = Image.objects.filter(house=house)
    receiver = house.seller
    sender = request.user
    form = MessageForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        chat = Chat.objects.create(sender=sender, receiver=receiver, house=house)
        message = Message.objects.create(sender=sender, house=house, receiver=receiver, chat=chat, **form.cleaned_data)
        return redirect('house:detail', house.pk)
    return render(request, 'detail.html', {'house': house, 'images': images, 'form': form})




def chat(request, pk):
    chat = Chat.objects.get(pk=pk)
    sender = request.user
    receiver = chat.receiver
    form = MessageForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        message = Message.objects.create(sender=sender, receiver=receiver,chat=chat, **form.cleaned_data)
        return redirect('house:chat', chat.pk)
    messages = Message.objects.filter(chat=chat)
    return render(request, 'chat.html', {'form': form,'messages':messages})


def chats(request):
    chats = Chat.objects.filter(sender=request.user,) | Chat.objects.filter(receiver=request.user)
    return render(request, 'chats.html', {'chats': chats})
