from django.shortcuts import render, HttpResponseRedirect,redirect,reverse
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
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
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.warning(request, "Invalid Login Details")

    context = {}
    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
