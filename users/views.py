from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile


def sign_up_page(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = form.save()
            avatar = form.cleaned_data.get('avatar')

            Profile.objects.create(user=user, avatar=avatar)

            return redirect('home_page')

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)
