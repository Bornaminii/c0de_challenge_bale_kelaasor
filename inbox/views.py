from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from inbox.models import inbox_messages


def inbox(request, username, password):
    user = User.objects.get(username=username, password=password)
    if user.password == password and user.username == username:
        messages = inbox_messages.objects.filter(reciver=request.user)
        return HttpResponse(messages)
    else:
        return HttpResponse("Invalid username or password")
