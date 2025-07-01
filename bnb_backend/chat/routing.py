from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    # path('ws/notification/', consumers.NotificationConsumer.as_asgi()),
    # path('ws/notification/<int:property_id>/', consumers.PropertyNotificationConsumer.as_asgi()),
]