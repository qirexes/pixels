# Generated by Django 5.1.4 on 2024-12-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_value', models.CharField(max_length=255, verbose_name='User Input')),
            ],
        ),
    ]
