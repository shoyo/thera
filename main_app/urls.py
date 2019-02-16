from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('<username>/journal/', views.journal, name='journal'),
    path('get_ip/',views.get_client_ip,name='client_id'),
    path('getting_help', views.getting_help, name='getting_help'),
    url(r'^login/$', auth_views.LoginView, name='login'),
    url(r'^logout/$', auth_views.LogoutView, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
