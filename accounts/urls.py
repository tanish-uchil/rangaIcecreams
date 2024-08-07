from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='loginUser'),
    path('signup/', views.signupUser, name='signupUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('updateUser/',views.updateUser, name='updateUser')
]
