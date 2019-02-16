from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('redirect/', views.redirect_view),
    path('<str:username>/journal', views.journal, name='journal'),
    path('signup/', views.signup, name='signup'),
    path('get_ip',views.get_client_ip,name='client_id'),
    # path('signin/', auth_views.login, name='login'),
    # path('signout/', auth_views.logout, name='logout'),
]
