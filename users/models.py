from django.db import models


class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=10)  # Adjusted max_length to 10 for mobile numbers
    email = models.EmailField(unique=True, max_length=100)  # Use EmailField for better validation
    locality = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)  # Use TextField for longer addresses
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='waiting')

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'user_registrations'

