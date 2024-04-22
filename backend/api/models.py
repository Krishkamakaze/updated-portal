from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class DetailsCOE(models.Model):
    studentName = models.CharField(max_length=50)
    fatherName = models.CharField(max_length=50)
    rollnumber = models.IntegerField()
    programme = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    mobilenumber = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    aadharnumber = models.IntegerField()
    nodues_copy = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])], blank=True , null = True)
    aadharcopy = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])], blank=True , null = True)
    status = models.CharField(max_length=20, default='processing')
    created_at = models.DateTimeField(default=timezone.now , verbose_name='Created At', help_text='IST time')
    Certificate = models.CharField(max_length=50)
    FIR_copy = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])], blank=True , null = True)
    newsadv = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])], blank=True , null = True)
    payment_ss = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])], blank=True , null = True)
    verified_by = models.CharField(max_length=15 , blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At', help_text='IST time')
    class Meta:
        ordering = ['-created_at']
