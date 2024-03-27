
from django.urls import path
from . import views

urlpatterns = [

    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
]