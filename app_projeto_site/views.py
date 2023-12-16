# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View

from app_projeto_site.forms import Cadastro
from .forms import UserCreationForm, ProfileForm


def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def profile_user(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Seu perfil foi atualizado com sucesso!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'profile-user.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, Você está logado!')
            return redirect('profile')
        else:
            messages.info(request, 'Senha ou usuário inválido!')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'Você saiu!')
    return redirect('login')


class RegisterView(View):
    form_class = Cadastro
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso por {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})



