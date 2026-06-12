from django.urls import path
from inbox.views import inbox, send_message, token_generator

urlpatterns = [
    path('list_messages/<str:username>/<str:password>/', inbox, name='inbox'),
    path('send_messages/<str:username>/<str:password>/', send_message, name='send-message'),
    path('user_token/<str:username>/<str:password>/', token_generator, name='token_generator')
]
