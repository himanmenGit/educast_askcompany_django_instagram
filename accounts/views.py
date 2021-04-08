from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, '회원가입 환영 합니다.')
            signed_user.send_welcome_email()
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form
    })
