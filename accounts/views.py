from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def logout_site(request):
  logout(request)
  messages.success(request, 'Usuário deslogado com sucesso!')
  return redirect('index')

def auth(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Usuário logado com sucesso!')
      return redirect('index')
    else:
      return redirect('auth')
  else:
    user_form_authentication = AuthenticationForm()
  return render(request, 'auth.html', context={'user_form_authentication': user_form_authentication})

def register(request):
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST)
    if user_form.is_valid():
      user_form.save()
      return redirect('auth')
    else:
      messages.error(request, 'Erro ao criar usuário')
      return redirect('register')
  else:
    user_form = UserCreationForm()
  return render(request, 'register.html', context={'user_form': user_form})
