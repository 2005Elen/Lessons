from django.urls import path
from .views import CategoryListView, LessonsByCategoryView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:category_slug>/', LessonsByCategoryView.as_view(), name='lessons_by_category'),
    path('lesson/new/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<slug:slug>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/<slug:slug>/edit/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<slug:slug>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
]
