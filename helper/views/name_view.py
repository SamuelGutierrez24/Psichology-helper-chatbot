from django.shortcuts import render,redirect

def name(request):
    if request.method == 'POST':
        name = request.POST['name']
        request.session['user_name'] = name
        return redirect('chat')
    else:
        return render(request,'name.html')