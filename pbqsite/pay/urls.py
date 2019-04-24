from django.urls import path
from pay import views

urlpatterns = [
    path('', views.PayView.as_view(), name='index'),
]
