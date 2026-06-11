from django.db import models
from django.contrib.auth.models import User


class mMessages(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE , related_name='sender')
    reciver = models.ForeignKey(User, on_delete=models.CASCADE , related_name='reciver')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message

