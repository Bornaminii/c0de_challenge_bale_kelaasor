from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from inbox.models import inbox_messages


def inbox(request, username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("Invalid username or password")

    if not user.check_password(password):
        return HttpResponse("Invalid username or password")

    messages = inbox_messages.objects.filter(reciver=user)
    content = "\n".join(str(m) for m in messages) or "No messages"
    return HttpResponse(content)
