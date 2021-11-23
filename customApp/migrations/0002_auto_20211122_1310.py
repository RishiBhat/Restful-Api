# Generated by Django 3.0 on 2021-11-22 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='Singer',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Singer',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]