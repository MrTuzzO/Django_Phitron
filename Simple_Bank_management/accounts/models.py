from django.contrib.auth.models import User
from django.db import models
from .constans import ACCOUNT_TYPE, GENDER_TYPE


class UserBankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE)
    account_number = models.IntegerField(unique=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE)
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.account_number}"


class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField(max_length=15)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email} {self.city} {self.postal_code} {self.country}"