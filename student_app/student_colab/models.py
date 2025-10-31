from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
<<<<<<< HEAD
    coureses = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
=======
    goal = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    stu_year = models.DateField()
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Module (models.Model):
    module_name = models.CharField(max_length=100)
    module_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
>>>>>>> 3acf5cfe946606ae718da517462e257cee0fb593

    def __str__(self):
        return f"{self.module_code}  {self.module_name}"
    
class stu_match(models.Model):
    student1 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='links_initiated')
    student2 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='links_received')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    