from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add',views.add),
    path('delete/<int:id>', views.delete),
    path('delete/<int:id>/remove', views.remove)
]
