from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.shortcuts import redirect, render
from .forms import SignupForm


# def login(request):
#     pass

login = LoginView.as_view(template_name="accounts/login_form.html")

def logout(request):
    messages.success(request, 'Log Out.')
    return logout_then_login(request)
    # 로그아웃 하자마자 로그인 페이지로 보내버리겠다.

# logout = LogoutView.as_view(template_name="accounts/logout_form.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "Welcome!")
            signed_user.send_welcome_email()    # FIXME: Celery로 비동기 처리하는 것 추천.
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form':form,
    })