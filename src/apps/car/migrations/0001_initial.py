# Generated by Django 5.1.1 on 2024-09-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100, verbose_name='марка')),
                ('model', models.CharField(max_length=100, verbose_name='модель')),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
