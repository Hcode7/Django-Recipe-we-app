from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import logout, login

# Create your views here.


# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegistration(request.POST)
#         if form.is_valid():
#             register = form.save(commit=False)
#             register.set_password(form.cleaned_data['password'])
#             register.save()
#             return redirect('login')
#     else:
#         form = UserRegistration()
#     return render(request, 'registration/register.html', {'form' : form})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistration()
    return render(request, 'registration/register.html', {'form' : form})


def logout_view(request):
    logout(request)
    return redirect('login')