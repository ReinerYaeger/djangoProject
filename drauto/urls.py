from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('client_login/', views.client_login, name='client_login'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_form, name='register'),
    path('contact/', views.contact, name='contact'),


    path('vehicle/', views.vehicle, name='vehicle'),
    path('vehicle/purchase/<str:vehicle_id>/', views.purchase, name='purchase'),
    # path('vehicle/purchase/<str:')
]