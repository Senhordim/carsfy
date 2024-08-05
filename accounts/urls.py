from django.urls import path
from .views import register, auth
urlpatterns = [
  path('register', register, name="register"),
  path('auth', auth, name="auth"),
]
