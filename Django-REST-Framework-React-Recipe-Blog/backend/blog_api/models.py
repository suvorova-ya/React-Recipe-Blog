from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255 ,verbose_name='Название')
    image = models.ImageField(upload_to='image', null=True, blank=True,verbose_name='Изображение')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.name

class blog(models.Model):
    POST_CHOICES = [
        ('POPULAR', 'Popular')
    ]
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True,verbose_name='Категория')
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    slug = models.SlugField(max_length=255)
    excerpt = models.CharField(max_length=255, default='',verbose_name='Отрывок')
    content = models.TextField(null=True, blank=True,verbose_name='Описание')
    contentTwo = models.TextField(null=True, blank=True,verbose_name='Описание')
    image = models.ImageField(upload_to='image', null=True, blank=True,verbose_name='Изображение')
    ingredients = models.TextField(null=True, blank=True,verbose_name='Ингредиенты')
    postlabel = models.CharField(max_length=100, choices=POST_CHOICES,null=True, blank=True)
    
    
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"

    def __str__(self):
        return self.title
