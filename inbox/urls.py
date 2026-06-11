from django.urls import path
from inbox.views import inbox

urlpatterns = [
    path('list_messages/<str:username>/<str:password>/', inbox, name='inbox'),
]
