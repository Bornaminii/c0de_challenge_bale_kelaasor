from django.urls import path
from inbox.views import inbox

urlpatterns = [
    path('list_messages/', inbox, name='inbox'),
]