from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=20)
    email=models.TextField()
    contact=models.IntegerField()
    class Meta:
        db_table="studentdb"