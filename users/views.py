from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def signin_done(request):
    return render(request, 'users/signin_done.html', status=500)
