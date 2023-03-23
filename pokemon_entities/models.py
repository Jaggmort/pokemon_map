from django.db import models  

class Pokemon(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title