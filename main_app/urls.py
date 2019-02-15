from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('redirect/', views.redirect_view),
    # path('signin/', auth_views.login, name='login'),
    # path('signout/', auth_views.logout, name='logout'),
]
