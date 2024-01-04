from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    designation=models.CharField(max_length=100)
    email_address=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=12,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
