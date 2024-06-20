from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    avatar = models.ImageField(upload_to="upload/%Y/%m", default=None)


class Category(models.Model):
    name =models.CharField(max_length=100,null=False, unique =True)


class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to="courses/%Y/%m", default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.subject

class Course(ItemBase):
    class Meta:
        unique_together = ('subject','category')
    description = models.TextField(null=True, blank=True)    
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Lesson(ItemBase):    
    class Meta:
        unique_together =('subject','courses')
    contents = RichTextField()  
    courses = models.ForeignKey(Course,related_name ="lessons", on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',related_name ="lessons", blank=True)
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)    
    
    def __str__(self):
        return self.name