from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def auth(request):
  user_form_authentication = AuthenticationForm()
  return render(request, 'auth.html', context={'user_form_authentication': user_form_authentication})

def register(request):
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST)
    if user_form.is_valid():
      user_form.save()
      return redirect('auth')
  else:
    user_form = UserCreationForm()
  return render(request, 'register.html', context={'user_form': user_form})
