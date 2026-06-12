from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from inbox.models import InboxMessages
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json


def inbox(request, username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("Invalid username")

    if not user.check_password(password):
        return HttpResponse("Password is not correct")

    messages = user.recived_messages.order_by("-id").all()
    return render(request, "inbox.html", {"messages": messages})

# @csrf_exempt
def send_message(request, username, password):

    if request.method == "GET":
        return render(request, "send_message.html")

    if request.method == "POST":
        try:
            sender_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse("Invalid username or password")

        if not sender_user.check_password(password):
            return HttpResponse("Invalid username or password")
        
        body = request.body
        reciever_username = request.POST.get("reciever_username")
        if not reciever_username:
            messages.error(request, "reciever_username is required")
            return render(request, "send_message.html")
        try:
            reciever_user = User.objects.get(username=reciever_username)
        except User.DoesNotExist:
            messages.error(request, "Invalid reciever_username")
            return render(request, "send_message.html")

        message = request.POST.get("message")
        if not message:
            messages.error(request, "message is required")
            return render(request, "send_message.html")

        create_massage(
            sender=sender_user,
            reciver=reciever_user,
            message=message,
        )

        messages.success(request, "Message sent successfully!")
        return render(request, "send_message.html")



def create_massage(sender, message, reciver):
    InboxMessages.objects.create(
        sender=sender,
        reciver=reciver,
        message=message
    )



def token_generator(request, username, password):

    user = User.objects.get(username=username)
    username = user.username
    list(username)
    pass_list = []

    for number in username:
        number_int = int(number)
        current = int(username[(number_int - 1) % len(username)])
        target = int(username[(current + number_int) % len(username)])
        new_num = number_int + int(target)
        pass_list.append(str(new_num))
    
    password_str = ''.join(pass_list)
        # print(password_str)
    return HttpResponse(password_str)





