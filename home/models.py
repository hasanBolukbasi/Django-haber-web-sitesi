from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


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
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.EmailField(blank=True)
    smtpserver = models.URLField(blank=True)
    smtpemail = models.EmailField(blank=True)
    smtppassword = models.CharField(blank=True, max_length=30)
    smtpport = models.IntegerField(blank=True, null=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    ip = models.GenericIPAddressField()
    status = models.CharField(max_length=10, choices=STATUS)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control p-4'}),
            'subject': TextInput(attrs={'class': 'form-control p-4'}),
            'email': TextInput(attrs={'class': 'form-control p-4'}),
            'message': Textarea(attrs={'class': 'form-control'}),
        }


class UserProfile(models.Model):
    USER_ROLE = (
        ('Kullanıcı', 'Kullanıcı'),
        ('Muhabir', 'Muhabir'),
        ('Yazar', 'Yazar'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')
    role = models.CharField(blank=True, max_length=10, choices=USER_ROLE)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '['+self.user.username + '] ' + self.user.first_name + ' ' + self.user.last_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country', 'image']
