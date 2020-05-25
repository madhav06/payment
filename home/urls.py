from django.urls import path
from . import views

urlpatterns = [
    path('', views.payme, name='payme'),
    path('payment/success', views.payment_success, name='payemnt_success'),
    path('payment/failure', views.payment_failure, name='payment_failure')
]
