from django.shortcuts import HttpResponse
from inbox.models import inbox_messages


def inbox(request):
    messages = inbox_messages.objects.filter(reciver=request.user)
    return HttpResponse(messages)
