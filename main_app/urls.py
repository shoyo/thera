from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('myjournal/', views.journal_index, name='myjournal'),
    path('<username>/journal/', views.journal, name='journal'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signin_attempt', views.signin_view, name='signin_attempt'),
    path('get_ip/',views.get_client_ip,name='client_id'),
    path('getting_help', views.getting_help, name='getting_help'),
]
