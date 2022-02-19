from django.urls import path, re_path
from . import views as v

# app_name = AppName

urlpatterns = [
    path('create',v.create, name='create'),
    path('read',v.read, name='read'),
    path('update/<int:id>',v.update, name='update'),
    path('delete/<int:id>',v.delete, name='delete'),
]