from django.db import models


class Settings(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    icon = models.ImageField(blank=True, upload_to='images/')
    company = models.CharField(blank=True, max_length=150)
    address = models.TextField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=10)
    fax = models.CharField(blank=True, max_length=10)
    email = models.EmailField(blank=True)
    smtpserver = models.URLField(blank=True)
    smtpemail = models.EmailField(blank=True)
    smtppassword = models.CharField(blank=True, max_length=30)
    smtpport = models.IntegerField(blank=True, null=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title
