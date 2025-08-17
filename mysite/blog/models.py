# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen_destacada = models.ImageField(
        upload_to='post_images/', blank=True, null=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})


class Comentario(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['fecha_creacion']
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.post.titulo}'
