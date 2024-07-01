from django.shortcuts import render
from usuarios.forms import LoginsForms, CadastroForms

def login(request):
    form = LoginsForms()
    return render(request, "usuarios/login.html",{'form':form})


def cadastro(request):
    form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {'form':form})

