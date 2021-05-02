from django.urls import include, path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signin_done/', views.signin_done, name='signin_done'),
    path('', include('django.contrib.auth.urls')),

]
