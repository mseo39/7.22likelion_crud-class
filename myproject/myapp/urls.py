from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('', myapp.views.home, name='home'),
    path('create/', myapp.views.create, name='create'),
    path('update/<int:item_id>', myapp.views.update, name='update'),
    path('delete/<int:item_id>', myapp.views.delete, name='delete'),
]