from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)
    created_at = models.DateField(auto_created=True, null=True)

    def __str__(self):
        return self.title