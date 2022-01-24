from django.db import models

# ---------------------- Creating a verdict model ---------------------- #

class Verdict(models.Model):
    stock = models.TextField()
    verdict = models.TextField()
    
    def __str__(self):
        return self.stock