from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Register
        pass
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login
        pass
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')