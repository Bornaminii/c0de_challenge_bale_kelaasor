from django.db import models
from django.contrib.auth.models import User


class InboxMessages(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE , related_name='sent_messages')
    reciver = models.ForeignKey(User, on_delete=models.CASCADE , related_name='recived_messages')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message

