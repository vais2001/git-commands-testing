from django.db import models
# import datetime

# Create your models here.
class Diary_model(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    # def __str__(self):
        # return self.content