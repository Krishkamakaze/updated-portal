# Generated by Django 5.0.3 on 2024-04-23 11:56

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_detailscoe_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailscoe',
            name='FIR_copy',
            field=models.FileField(blank=True, null=True, upload_to='FIRfile', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='detailscoe',
            name='aadharcopy',
            field=models.FileField(blank=True, null=True, upload_to='aadharfile', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='detailscoe',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='IST time', verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='detailscoe',
            name='newsadv',
            field=models.FileField(blank=True, null=True, upload_to='newsadvFile', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='detailscoe',
            name='nodues_copy',
            field=models.FileField(blank=True, null=True, upload_to='noduesfile', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='detailscoe',
            name='payment_ss',
            field=models.FileField(blank=True, null=True, upload_to='Paymentfile', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='detailscoe',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='processing', max_length=20),
        ),
        migrations.AlterField(
            model_name='detailscoe',
            name='verified_by',
            field=models.CharField(choices=[('COE', 'COE'), ('DAA', 'DAA')], max_length=15),
        ),
    ]
