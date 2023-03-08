from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login_form/', views.login_form, name='login_form'),
    path('logout/', views.logout_user, name='logout')

]