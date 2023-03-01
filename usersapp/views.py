from .forms import UserRegisterForm
from .forms import UserForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


class LoginView(View):

    def get(self, request):
        form = UserForm()
        if "sign-in" in request.GET:
            username = request.GET.get("username")
            password = request.GET.get("pswd")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Login attemp failed.')
                return redirect('account_login')
        return render(request, './templates/login.html', {'form': form})

    def post(self, request):
        if "sign-up" in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                selected_group = request.POST.get("groups")
                group = Group.objects.get(name=selected_group)
                user.groups.add(group)
                messages.success(request, 'Account has been created succesfully')
                return redirect('account_login')
            else:
                messages.error(request, form.errors)
                return redirect('account_login')
        return render(request, './templates/login.html')


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out succesfully.')
        return redirect('account_login')


