from django.shortcuts import render, redirect

def logout(request):
    del request.session['user_name']
    return redirect('name')