
from django.urls import path    
from .views import home, contact, about, item_detail

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path("item/<int:id>/", item_detail, name="item_detail"),
]




