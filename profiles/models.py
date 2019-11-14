from django.db import models
from datetime import datetime, timezone

# ----------------------User Account

class User_Photo(models.Model):
    user_account_id = models.ForeignKey('User_Account', on_delete=models.CASCADE, related_name='user_photos')
    link = models.TextField()
    details = models.TextField()
    date_time_added = models.DateTimeField()
    active = models.BooleanField(default=True)

class Pet_Photo(models.Model):
    user_account_id = models.ForeignKey('User_Account', on_delete=models.CASCADE, related_name='pet_photos')
    link = models.TextField()
    details = models.TextField()
    date_time_added = models.DateTimeField()
    active = models.BooleanField(default=True)
    
class User_Account(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender_id = models.ForeignKey('Gender', on_delete=models.CASCADE, related_name='user_accounts')
    pet_photo_id = models.ForeignKey('Pet_Photo', on_delete=models.CASCADE, related_name='user_accounts')
    details = models.TextField()
    nickname = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    

class Interested_In_Gender(models.Model):
    user_account_id = models.ForeignKey('User_Account', on_delete=models.CASCADE, related_name='interested_in_genders')
    gender_id = models.ForeignKey('Gender', on_delete=models.CASCADE, related_name='interested_in_genders')

class Gender(models.Model):
    nam = models.CharField(max_length=32)

# ----------------------------Conversation

class Conversation(models.Model):
    user_account_id = models.ForeignKey('User_Account', on_delete=models.CASCADE, related_name='conversations')
    time_started = models.TimeField()
    time_closed = models.TimeField()

class Participant(models.Model):
    coversation_id = models.ForeignKey('Conversation', on_delete=models.CASCADE, related_name ='participants')
    user_account_id = models.ForeignKey('User_Account', on_delete=models.CASCADE, related_name ='participants')
    time_joined = models.TimeField()
    time_left = models.TimeField()

class Message(models.Model):
    participant_id = models.ForeignKey('Participant', on_delete=models.CASCADE, related_name='messages')
    message_text = models.TextField()
    time_stamp = models.TimeField()








    
