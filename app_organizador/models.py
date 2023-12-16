from datetime import date
from django.db import models
from app_projeto_site.models import models


class Organizador(models.Model):

    palestrante = models.CharField(default='Palestrante Default', max_length=50, null=True)
    
    titulo =models.CharField(default='Titulo Default', max_length=200, null=True)

    desc = models.CharField(default='Descrição Default', max_length=500, null=True)

    link = models.URLField(default='Link Default', max_length=100, null=True)

    data = models.DateField(default=date.today(), null=True)

    evento_img = models.ImageField(default='media/default.jpg', upload_to = 'media', null =True)

    def __str__(self):
        return f'Organizador do evento - {self.palestrante}'



