# Generated by Django 4.0.3 on 2022-04-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictionaryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alphabet', models.CharField(max_length=1)),
                ('word', models.CharField(max_length=30)),
                ('definition', models.CharField(max_length=300)),
                ('example', models.CharField(max_length=300)),
            ],
        ),
    ]
