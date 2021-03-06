from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'wall_messages': Wall_Message.objects.all()
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

def post_mess(request):
    Wall_Message.objects.create(message=request.POST['mess'], poster=User.objects.get(id=request.session['id']))
    return redirect('/success')

def post_comment(request, id):
    #create
    poster = User.objects.get(id=request.session['id'])
    message = Wall_Message.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/success')

def profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'profile.html', context)

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/success')

def destroy(request, id):
    deleted_post = Wall_Message.objects.get(id=id)
    deleted_post.delete()
    return redirect('/success')

def edit_page(request, id):
    context = {
        'edit_mess': Wall_Message.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def process_edit(request, id):
    mess_edit = Wall_Message.objects.get(id=id)
    mess_edit.message = request.POST['message']
    mess_edit.save()
    return redirect('/success')