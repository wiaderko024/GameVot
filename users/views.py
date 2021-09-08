from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile
from categories.models import Category


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
