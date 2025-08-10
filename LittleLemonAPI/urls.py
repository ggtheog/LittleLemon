# LittleLemonAPI/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name= 'menuitems'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),  # to obtain token via username/password
    
]
