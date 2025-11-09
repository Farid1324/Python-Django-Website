from django.urls import path
from . import views

urlpatterns = [
    path('sendtelegram/', views.send_telegram, name='send_telegram'),
    # Add other paths as needed
]
