from django.urls import path
from inbox.views import inbox, send_message

urlpatterns = [
    path('list_messages/<str:username>/<str:password>/', inbox, name='inbox'),
    path('send_messages/<str:username>/<str:password>/', send_message, name='send-message'),
]
