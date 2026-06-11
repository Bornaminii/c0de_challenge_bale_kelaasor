from django.contrib.admin import ModelAdmin, register
from inbox.models import inbox_messages

@register(inbox_messages)
class inbox_messagesAdmin(ModelAdmin):
    list_display = ['id', 'message', 'sender', 'reciver', 'created_at']
    list_filter = ['sender', 'reciver', 'created_at']
    search_fields = ['message', 'sender__username', 'reciver__username']