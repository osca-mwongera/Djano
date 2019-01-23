from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect


from .forms import SignUpForm


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/registration.html', {'form': form})
