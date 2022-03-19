from django.db import models

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Payment(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Document(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Ticket(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
class UserProfile(models.Model):
    pass


class User(models.AbstractUser):
    profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, primary_key=True)
