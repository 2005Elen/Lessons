from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    lesson_description = models.TextField()
    lesson_image = models.ImageField(upload_to='media/', blank=True, null=True)
    teacher_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.lesson_name