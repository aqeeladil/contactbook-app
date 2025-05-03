from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('view/<int:pk>/', views.view_contact, name='view_contact'),
    path('update/<int:pk>/', views.update_contact, name='update_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('register/', views.register, name='register'),
]
