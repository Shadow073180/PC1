from django.db import models
from datetime import datetime, timezone

# ----------------------User Account

class User(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    picture = models.ImageField()
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, related_name='users')
    

    def __str__(self):
        return f'First:{self.first_name} Last:{self.last_name} Pet:{self.pet}'

class Pet(models.Model):
    name = models.CharField(max_length=65)
    
    def __str__(self):
        return self.name

class Match(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='matches')

    def __str__(self):
        return self.user_id









    
