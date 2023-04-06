from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    qty = models.IntegerField()
    author = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "book"
