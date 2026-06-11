from django.contrib.auth.models import User
from django.http import HttpResponse
from inbox.models import inbox_messages


def inbox(request, username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("Invalid username or password")

    if not user.check_password(password):
        return HttpResponse("Invalid username or password")

    messages = inbox_messages.objects.filter(reciver=user)
    txt = ''
    for message in messages:
        txt += f"message: {message.message}, sender: {message.sender}\n"
    return HttpResponse(txt)


def send_massage(request, username, password, reciver_username, message):
    try:
        sender_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("Invalid username or password")

    if not sender_user.check_password(password):
        return HttpResponse("Invalid username or password")

    # body = request.POST
    # message = body.get("message")
    # reciever_username = body.get("target_username")

    try:
        reciever_user = User.objects.get(username=reciver_username)
    except User.DoesNotExist:
        return HttpResponse("Invalid reciver_username")

    create_massage(
        sender=sender_user,
        reciver=reciever_user,
        message=message,
    )

    return HttpResponse("Message sent successfully")


def create_massage(sender, message, reciver):
    inbox_messages.objects.create(
        sender=sender,
        reciver=reciver,
        message=message
    )
