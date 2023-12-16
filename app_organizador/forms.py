from django.forms import ModelForm
from django.forms.widgets import FileInput, DateInput, Textarea
from app_organizador.models import Organizador


class OrganizadorForm(ModelForm):
    class Meta:
        model = Organizador
        fields = '__all__'
        exclude = ['buscar']
        widgets = {
            'evento_img': FileInput(),
            'data' : DateInput(),
            'desc' : Textarea(),
            }
            