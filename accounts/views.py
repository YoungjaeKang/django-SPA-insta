from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignupForm


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, "Welcome!")
            signed_user.send_welcome_email()    # FIXME: Celery로 비동기 처리하는 것 추천.
            next_url = request.GET.get('next', '/')
            return redirect("next_url")
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form':form,
    })