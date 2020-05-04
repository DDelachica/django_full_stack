from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'book_list': Book.objects.all()
    }
    return render(request, 'success.html', context)

def register(request):
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')   
    new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['pw'])
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/success')

def login(request):
    print(request.POST)
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pw']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')

def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'], uploaded_by=User.objects.get(id=request.session['id']))
    return redirect('/success')

def book(request, id):
    context = {
        'user': User.objects.get(id=id),
        'books': Book.objects.all()
    }
    return render(request, 'book.html', context)

def add_favorite(request, id):
    favorite_book = Book.objects.get(id=id)
    user_favoriting = User.objects.get(id=request.session['id'])
    favorite_book.users_who_like.add(user_favoriting)
    return redirect('/success')

def destroy(request, id):
    deleted_book = Book.objects.get(id=id)
    deleted_book.delete()
    return redirect('/book_profile')


def edit_book(request, id):
    book_edit = Book.objects.get(id=id)
    book_edit.title = request.POST['title']
    book_edit.desc = request.POST['desc']
    book_edit.save()
    return redirect(f'/book_profile/{{id}}')