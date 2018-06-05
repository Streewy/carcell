from django.contrib.auth import login, authenticate
from messaging.forms import *
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', locals())


def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            customer = Customer()
            customer.owner = user
            customer.first_name = form.cleaned_data['first_name']
            customer.last_name = form.cleaned_data['last_name']
            customer.email = form.cleaned_data['email']
            if form.cleaned_data['plate_number']:
                customer.plate_number = form.cleaned_data['plate_number']
            customer.save()
            return redirect('/')
        else:
            return HttpResponse(form.errors)
    else:
        return render(request, 'registration/register.html', {'form': form})

def messages(request):
    my_messages = Message.objects.all()
    return render(request, 'messages.html', locals())

def send_message(request):
    form = MessageSendingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            sender = form.cleaned_data.get('sender')
            plate = form.cleaned_data.get('plate')
            content = form.cleaned_data.get('content')
            customer = Customer.objects.get(owner__username=sender)
            message = Message()
            message.sender = customer
            message.plate = plate
            message.content = content
            message.save()
            return redirect('message_sent')
        # else:
            # return HttpResponse(form.errors)
    else:
        return render(request, 'send_message.html', {'form': form})

def message_sent(request):
    return render(request, 'message_sent.html', locals())
