from django.urls import path
from .views import register, auth, logout_site
urlpatterns = [
  path('register', register, name="register"),
  path('auth', auth, name="auth"),
  path('logout', logout_site, name="logout"),
]
