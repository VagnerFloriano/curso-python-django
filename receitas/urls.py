from django.urls import path
from receitas.views import home  # Import views from the receitas app

urlpatterns = [
    path('', home),
]