from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # Поле внешний ключ отношение Один ко Многим 
    body =models.TextField()
    publish = models.DateTimeField(default=timezone.now) #Возвращает текущую дату и время
    created = models.DateTimeField(auto_now_add=True) # Автоматическое сохранение даты и времени при создании объекта
    updated = models.DateTimeField(auto_now=True) # Дата и время редактирования статьи
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
