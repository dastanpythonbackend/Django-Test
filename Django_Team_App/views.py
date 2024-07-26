from django.shortcuts import render, redirect
from .forms import UserRegister


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form': form})