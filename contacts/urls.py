from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact_us/', views.send_message, name='contact'),
]
