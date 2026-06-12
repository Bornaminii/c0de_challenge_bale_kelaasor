from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from inbox.models import InboxMessages
from django.views.decorators.csrf import csrf_exempt
import json


def inbox(request, username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("Invalid username")

    if not user.check_password(password):
        return HttpResponse("Password is not correct")

    messages = user.recived_messages.order_by("id").all()
    return render(request, "inbox.html", {"messages": messages})

@csrf_exempt
def send_massage(request, username, password):
    # Validate sender user
    try:
        sender_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("Invalid username or password")

    if not sender_user.check_password(password):
        return HttpResponse("Invalid username or password")

    # Get body of request
    body = json.loads(request.body)
    
    # Validate reciever user
    reciever_username = body.get("reciever_username")
    if not reciever_username:
        return HttpResponse("reciever_username is required")
    try:
        reciever_user = User.objects.get(username=reciever_username)
    except User.DoesNotExist:
        return HttpResponse("Invalid reciver_username")
    
    # Validate message
    message = body.get("message")
    if not message:
        return HttpResponse("message is required")

    create_massage(
        sender=sender_user,
        reciver=reciever_user,
        message=message,
    )

    return HttpResponse("Message sent successfully")


def create_massage(sender, message, reciver):
    InboxMessages.objects.create(
        sender=sender,
        reciver=reciver,
        message=message
    )
