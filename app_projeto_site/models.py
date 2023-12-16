from django.db import models
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(default = 'Nome', max_length=50, null=True)

    curso = models.CharField(default = 'Texto padrão para o curso.', max_length=200, null=True)

    desc_text = 'Texto padrão para descrição da bio.'

    bio = models.CharField(default = desc_text, max_length=200, null=True)

    profile_img = models.ImageField(default = 'media/default.png', upload_to = 'media', null = True, blank = True)

    def __str__(self):
        return f"{self.user.username} profile"
    
