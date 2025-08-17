# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Count  # Import para filtrar por comentarios
from .models import Post, Categoria, Comentario
from .forms import PostForm, ComentarioForm
import datetime  # Para filtrar por fecha


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar por categoría
        categoria_nombre = self.request.GET.get('categoria')
        if categoria_nombre:
            queryset = queryset.filter(categoria__nombre=categoria_nombre)

        # Filtrar por fecha
        fecha_str = self.request.GET.get('fecha')
        if fecha_str:
            try:
                fecha_obj = datetime.datetime.strptime(
                    fecha_str, '%Y-%m-%d').date()
                queryset = queryset.filter(fecha_publicacion__date=fecha_obj)
            except ValueError:
                pass  # Ignorar fecha inválida

        # Ordenar por número de comentarios (ejemplo de filtro/ordenamiento avanzado)
        ordenar_por_comentarios = self.request.GET.get('ordenar_comentarios')
        if ordenar_por_comentarios == 'asc':
            queryset = queryset.annotate(num_comentarios=Count(
                'comentarios')).order_by('num_comentarios')
        elif ordenar_por_comentarios == 'desc':
            queryset = queryset.annotate(num_comentarios=Count(
                'comentarios')).order_by('-num_comentarios')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()
        context['comment_form'] = ComentarioForm()
        return context


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    # Redirige al home después de crear
    success_url = reverse_lazy('blog:home')

    # Nuevo método para verificar los permisos
    def test_func(self):
        # La condición es que el usuario debe ser un superusuario o un staff
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asigna el autor al usuario logueado
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # Solo el autor o un superusuario puede actualizar el post
        return self.request.user == post.autor or self.request.user.is_superuser


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:home')

    def test_func(self):
        post = self.get_object()
        # Solo el autor o un superusuario puede eliminar el post
        return self.request.user == post.autor or self.request.user.is_superuser


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.autor = request.user  # Asigna el autor al usuario logueado
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        # Esto no debería ocurrir si se accede solo por POST
        return redirect('blog:post_detail', pk=post.pk)
