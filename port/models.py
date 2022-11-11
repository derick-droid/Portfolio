from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    project_link = models.URLField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")