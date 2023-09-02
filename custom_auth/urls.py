from django.urls import path
from .views import SMSLoginViewSet

urlpatterns = [
    path('send-sms/', SMSLoginViewSet.as_view({'post': 'send_sms'}), name='send_sms'),
    path('verify-sms/', SMSLoginViewSet.as_view({'post': 'verify_sms'}), name='verify_sms'),
]
