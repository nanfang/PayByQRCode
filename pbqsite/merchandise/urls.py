from django.urls import path
from django.conf.urls import url
from merchandise import views, messaging

urlpatterns = [
    path('', views.index, name='index'),
]


websocket_urlpatterns = [
    url(r'^merchandise/payment/$', messaging.PaymentConsumer),
]
