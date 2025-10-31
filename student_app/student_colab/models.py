from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class module (models.Model):
    module_name = models.CharField(max_length=100)
    module_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.module_code} - {self.module_name}"
    

    