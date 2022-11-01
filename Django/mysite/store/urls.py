from django.urls import path
from .views import example
# Create your tests here.

urlpatterns = [
    path ('', example, name='example')
]
