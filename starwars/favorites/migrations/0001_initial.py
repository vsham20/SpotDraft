# Generated by Django 3.2.9 on 2021-11-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('edited', models.DateTimeField()),
                ('url', models.CharField(max_length=500)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
