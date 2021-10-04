from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, ChangeAvatarForm, ChangePasswordForm
from .models import Profile
from categories.models import Category


def login_page(request):
    categories = Category.objects.all()
    form = LoginForm()

    if request.method == 'POST':
        if request.POST.get('search') is not None:
            return redirect('search_page', request.POST.get('search'))

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
        if request.POST.get('search') is not None:
            return redirect('search_page', request.POST.get('search'))

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


@login_required
def user_dashboard(request):
    categories = Category.objects.all()
    user = request.user
    form = SignUpForm(instance=user)

    if request.method == 'POST':
        if request.POST.get('search') is not None:
            return redirect('search_page', request.POST.get('search'))

        form = SignUpForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'dashboard.html', context)


@login_required
def change_avatar(request):
    categories = Category.objects.all()
    form = ChangeAvatarForm()

    if request.method == 'POST':
        if request.POST.get('search') is not None:
            return redirect('search_page', request.POST.get('search'))

        form = ChangeAvatarForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = request.user
            avatar = form.cleaned_data.get('avatar')

            user.profile.avatar = avatar
            user.profile.save()
            
            return redirect('users:dashboard')

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'avatar.html', context)


@login_required
def change_password(request):
    categories = Category.objects.all()
    form = ChangePasswordForm()

    if request.method == 'POST':
        if request.POST.get('search') is not None:
            return redirect('search_page', request.POST.get('search'))

        form = ChangePasswordForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            user = request.user

            user.set_password(password)
            user.save()

            return redirect('home_page')

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'password.html', context)
