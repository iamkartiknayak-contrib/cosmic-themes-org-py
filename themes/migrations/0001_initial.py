# Generated by Django 5.1 on 2024-08-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ron', models.TextField()),
                ('css', models.TextField(blank=True, default='')),
                ('author', models.CharField(blank=True, default='', max_length=200)),
                ('link', models.URLField(blank=True, default='')),
                ('downloads', models.PositiveIntegerField(blank=True, default=0, editable=False)),
                ('approved', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
