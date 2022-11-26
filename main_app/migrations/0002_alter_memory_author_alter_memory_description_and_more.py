# Generated by Django 4.1.3 on 2022-11-25 04:09

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]