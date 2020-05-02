from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    context = {
        'gold': request.session['gold'],
        'message': request.session['message'],
        } 
    return render(request, 'index.html', context)

def process(request):
    if request.POST['action'] == "farm":
        earnings = random.randrange(10, 20)
        request.session['gold'] += earnings
        request.session['earnings'] = earnings
        request.session['message'] = "Earned " + str(request.session['earnings'])+" gold from the farm!"
        print(earnings)
        return redirect('/')
    if request.POST['action'] == "cave":
        earnings = random.randrange(5, 10)
        request.session['gold'] += earnings
        request.session['earnings'] = earnings
        request.session['message'] = "Earned " + str(request.session['earnings'])+ " gold from the farm!"
        print(earnings)
        return redirect('/')
    if request.POST['action'] == "house":
        earnings = random.randrange(2, 5)
        request.session['gold'] += earnings
        request.session['earnings'] = earnings
        request.session['message'] = "Earned " + str(request.session['earnings'])+ " gold from the farm!"
        print(earnings)
        return redirect('/')
    if request.POST['action'] == "casino":
        earnings = random.randrange(-50, 50)
        request.session['gold'] += earnings
        request.session['earnings'] = earnings
        if earnings > 0:
            request.session['message'] = "Entered a casino and won " + str(request.session['earnings'])+ " gold!"
        else:
            request.session['message'] = "Entered a casino and lost " + str(request.session['earnings']*-1)+ " gold!"
        print(earnings)
        return redirect('/')