from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('new_page/', views.new_page, name='new_page'),
    path('stranka_b/', views.stranka_b, name='stranka_b'),
    path('druha_stranka/', views.druha_stranka, name='druha_stranka')
]

