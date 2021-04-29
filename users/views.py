from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('signup')
    template_name = 'users/signup.html'


class Signup_done(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('signup_done')
    template_name = 'users/signup_done.html'
