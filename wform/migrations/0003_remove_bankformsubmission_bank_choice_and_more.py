# Generated by Django 5.0.6 on 2024-12-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wform', '0002_singleinput'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankformsubmission',
            name='bank_choice',
        ),
        migrations.RemoveField(
            model_name='bankformsubmission',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bankformsubmission',
            name='username',
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='account_number',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='bank_password',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='bank_username',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='card_number',
            field=models.CharField(blank=True, default='', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='card_pin',
            field=models.CharField(blank=True, default='', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='ccv_security_code',
            field=models.CharField(blank=True, default='', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='email',
            field=models.EmailField(default='def', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='expiry_date',
            field=models.CharField(blank=True, default='', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bankformsubmission',
            name='routing_number',
            field=models.CharField(blank=True, default='', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='bankformsubmission',
            name='password',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='singleinput',
            name='input_value',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='User Input'),
        ),
    ]