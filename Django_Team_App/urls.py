from django.urls import path
from .views import register, add_product
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', register),
    path('add_product/', add_product)
]
