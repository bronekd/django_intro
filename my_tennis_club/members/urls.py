from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('new_page/', views.new_page, name='new_page'),
]

