from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin # Цей міксін перевіряє чи авторизований юзер на сайті
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .forms import *


class RegisterUser( CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    # success_url = reverse_lazy('users:login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Реєстрація")
    #     return context | c_def
    #
    def form_valid(self, form): #Метод викликається коли успішно заєрестравався
        user = form.save()
        login(self.request, user) # Авторизлвує користавача
        return redirect('shop:product_list')


class LoginUser( LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Авторизація')
    #     return dict(list(context.items()) + list(c_def.items()))
    #
    def get_success_url(self):
        return reverse_lazy('shop:product_list')

def logout_user(request):
    logout(request)
    return redirect('users:login')