from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login_form/', views.login_form, name='loginform'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_form, name='register'),
    path('contact/', views.contact, name='contact'),
    path('vehicle/', views.vehicle, name='vehicle'),

]