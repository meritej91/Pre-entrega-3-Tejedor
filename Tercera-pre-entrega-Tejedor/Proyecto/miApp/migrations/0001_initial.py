# Generated by Django 4.2.5 on 2023-09-25 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('especie', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
