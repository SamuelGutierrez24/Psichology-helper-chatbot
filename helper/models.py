from django.db import models

class Message(models.Model):
    question = models.CharField(max_length=1024, default="")
    text = models.CharField(max_length=1024)
    number = models.IntegerField(default=0)
    user_name = models.CharField(max_length=1024, default="")

    def __str__(self):
        return self.text
    
class diagnosis(models.Model):
    user_name = models.CharField(max_length=1024, default="")
    text = models.CharField(max_length=1024, default="")
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.text
