from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from .models import Profile
from categories.models import Category


def login_page(request):
    categories = Category.objects.all()
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('users:login')


def sign_up_page(request):
    categories = Category.objects.all()
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = form.save()
            avatar = form.cleaned_data.get('avatar')

            Profile.objects.create(user=user, avatar=avatar)

            return redirect('home_page')

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'signup.html', context)


def user_dashboard(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'dashboard.html', context)
