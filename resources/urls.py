from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('share/', views.share_resource, name='share_resource'),
]
