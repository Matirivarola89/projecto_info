# blog/admin.py

from django.contrib import admin
from .models import Post, Categoria, Comentario

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
