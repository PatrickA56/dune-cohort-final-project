from django.contrib.auth import views as auth_view 
from django.urls import path 
from .import views 


urlpatterns = [
    path('accounts/login', auth_views.LoginView.asview(template_name='accounts/login.html')),
    path('accountslogout/', views.register, name='register'),
    path('accounts/', views.register, name='register'),
]
