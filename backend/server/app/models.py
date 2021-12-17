from django.contrib.auth.models import User
from django.db import models
import datetime


User._meta.get_field('email')._unique = True
User.EMAIL_FIELD = 'email'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    description = models.TextField(null=True)
    rating = models.FloatField(default=0)
    company = models.TextField()
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.user.email


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer', default=1)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor', default=1)
    title = models.TextField()
    description = models.TextField(null=True)
    rating = models.FloatField(null=True)
    review = models.TextField(null=True)
    deadline = models.DateTimeField(null=False, default=datetime.datetime.now)
    STATUS = [
        (0, 'opened'),
        (1, 'returned'),
        (2, 'closed'),
        (3, 'expects')
    ]
    status = models.IntegerField(choices=STATUS, default=0)
    comment = models.TextField(null=True)


class Technology(models.Model):
    user = models.ManyToManyField(User, related_name='technology')
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name
