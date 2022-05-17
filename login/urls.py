from django.urls import path
from .views import registration_view, login_view,home
urlpatterns = [
    path('',registration_view,name='registration'),
    path('login',login_view,name='login_page'),
    path('home',home,name='dashboard'),
]
