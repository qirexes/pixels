# Generated by Django 5.0.6 on 2024-06-05 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pix', '0006_image_name_image_price_image_upload_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pix.image')),
            ],
        ),
    ]
