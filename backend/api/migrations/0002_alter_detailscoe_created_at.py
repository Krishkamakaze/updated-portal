# Generated by Django 5.0.3 on 2024-04-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailscoe',
            name='created_at',
            field=models.DateTimeField(auto_now=True, help_text='IST time', verbose_name='Created At'),
        ),
    ]