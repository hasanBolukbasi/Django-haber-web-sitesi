from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    commment = models.TextField()
    rate = models.IntegerField()
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commment


class News(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    TUR = (
        ('Haber', 'Haber'),
        ('Köşe Yazısı', 'Köşe Yazısı'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    detail = models.TextField()
    type = models.CharField(max_length=20, choices=TUR)
    slug = models.SlugField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class User(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    USER_ROLE = (
        ('Kullanıcı', 'Kullanıcı'),
        ('Muhabir', 'Muhabir'),
        ('Yazar', 'Yazar'),
    )
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=USER_ROLE)
    # models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')
    address = models.TextField(max_length=255)
    phone = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone


class Images(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Faq(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Message(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    Ip = models.GenericIPAddressField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
