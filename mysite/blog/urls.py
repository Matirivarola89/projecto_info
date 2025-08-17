# blog/urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'blog'  # Espacio de nombres para las URLs

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
]
