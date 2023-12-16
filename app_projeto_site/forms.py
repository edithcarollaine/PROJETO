from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
from django.forms.models import ModelForm

from django.forms.widgets import FileInput

class Cadastro(UserCreationForm):
    first_name = forms.CharField(max_length=50,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Nome',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Sobrenome',
                                                            'class': 'form-control',
                                                            }))
    username = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Usuário',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                        'class': 'form-control',
                                                        }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Senha',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a senha',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {'profile_img': FileInput(),}

