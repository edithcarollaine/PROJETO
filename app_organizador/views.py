from django.shortcuts import render
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from app_organizador.forms import OrganizadorForm
from app_organizador.models import Organizador

@login_required(login_url='login')
def evento(request):
    if request.method == 'POST':
        form = OrganizadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        return redirect('cursos')
        
    else:
        form = OrganizadorForm()
        
    context = {'form':form}

    return render(request, 'organizador/criar.html', context)

@login_required(login_url='login')
def lista(request):

    cursos = Organizador.objects.all() 
    return render(request, 'organizador/cursos.html', context={'cursos':cursos})