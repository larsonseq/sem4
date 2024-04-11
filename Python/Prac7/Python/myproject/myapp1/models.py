from django.db import models

# Create your models here.
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.hashers import check_password 

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    passw = models.CharField(max_length=128, blank=True, null=True)  
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.passw = make_password(raw_password)

    @classmethod 
    def authenticate(cls, username, passw):
        try:
            user = cls.objects.get(username=username)
            print(f"Provided password: {passw}")
            print(f"Stored hashed password: {user.passw}")
            # if check_password(password, user.passw):
            if user.passw == passw:
                print("auth success")
                return user
        except cls.DoesNotExist:
            return None
        return None



