from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['category', 'lesson_name', 'lesson_description',
                  'lesson_image', 'teacher_name', 'price']
        exclude = ['slug']


