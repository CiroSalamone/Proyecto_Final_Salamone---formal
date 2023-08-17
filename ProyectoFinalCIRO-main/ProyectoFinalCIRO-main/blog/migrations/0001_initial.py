# Generated by Django 4.2.3 on 2023-08-15 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('subtitulo', models.CharField(max_length=256)),
                ('cuerpo', models.TextField(blank=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null='True', upload_to='entradas/')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
