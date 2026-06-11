from django.urls import path
from inbox.views import inbox, send_massage

urlpatterns = [
    path('list_messages/<str:username>/<str:password>/', inbox, name='inbox'),
    path('send_messages/<str:username>/<str:password>/<str:reciver_username>/<str:message>', send_massage, name='send-message'),
]
