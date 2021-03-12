from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup_done/', views.Signup_done.as_view(), name='signup_done'),
]
