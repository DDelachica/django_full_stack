from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('book_profile/<int:id>', views.book),
    path('add/<int:id>', views.add_favorite),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit_book)
]
