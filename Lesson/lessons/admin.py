from django.contrib import admin
from .models import Category, Lesson

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'category', 'teacher_name', 'price')
    search_fields = ('lesson_name', 'teacher_name', 'category__name')
    prepopulated_fields = {'slug': ('lesson_name',)}
