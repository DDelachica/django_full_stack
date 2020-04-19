from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from django.contrib import messages

def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        return redirect('/')

def delete(request, id):
    course = Course.objects.get(id=id)
    context = {
        'this_course': course
    }
    return render(request, 'delete.html', context)

def remove(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')