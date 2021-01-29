from django.urls import path
from .views import HomePageView, OrderView, AboutUsView, ContactView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('order/', OrderView.as_view(), name='order'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact/', ContactView, name='contact')
]