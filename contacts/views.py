from django.conf import settings
from django.shortcuts import render
from pyexpat.errors import messages
from django.contrib import messages


from .models import Info
from django.core.mail import send_mail




def send_message(request):
    myinfo=Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        user_message = request.POST['message']  # ✅ استخدم اسم مختلف عن 'messages'

        try:
            send_mail(
                subject,
                user_message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success( request, 'Message sent successfully!' )
        except Exception as e:
            messages.error( request, f'Error: {str( e )}' )
    return render(request, 'contact/contactus.html', {'myinfo':myinfo})