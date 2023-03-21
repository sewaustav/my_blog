from django.urls import path
from .views import *

urlpatterns=[
    path('blog', blog, name='blog'),
    path('favorite', favorite, name='favorite'),
    path('profile', profile, name='profile'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('portfolio', portfolio, name='portfolio'),
]