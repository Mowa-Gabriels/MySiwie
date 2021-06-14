from django.shortcuts import render, HttpResponseRedirect,redirect,reverse
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm
from django.urls import reverse_lazy

# Create your views here.
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('profile')
    template_name = 'authentication/profile_passwordedit.html'


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()



            return redirect('login')

    else:
        form = SignUpForm()

    return render(request, 'authentication/signup.html',{
            'form': form}
        )


def login_user(request):
    context = {}
    return render(request, 'authentication/login.html', context)


def login_validate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.success(request, "Invalid Login Details", extra_tags='alert alert-success')

    context = {}
    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
