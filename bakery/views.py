from django.shortcuts import render
from django.http import request
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class OrderView(TemplateView):
    template_name = 'order.html'


class AboutUsView(TemplateView):
    template_name = 'about.html'


def ContactView(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        msg_mail = str(message) + " " + str(message_email)

        send_mail(
            "Contacted by " + message_name,
            msg_mail, 
            message_email, 
            [settings.EMAIL_HOST_USER],
            fail_silently=False
            )
        return render(request, 'contact.html', {'message_name':message_name,
                                                'message_email': message_email,
                                                'message': message})
    else:
        return render(request, 'contact.html', {})
