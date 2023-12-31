# Generated by Django 4.2.7 on 2023-12-14 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_organizador', '0007_alter_organizador_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizador',
            name='data',
            field=models.DateField(default=datetime.date(2023, 12, 14), null=True),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='evento_img',
            field=models.ImageField(default='media/default.jpg', null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='link',
            field=models.URLField(default='Link Default', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='palestrante',
            field=models.CharField(default='Palestrante Default', max_length=50, null=True),
        ),
    ]
