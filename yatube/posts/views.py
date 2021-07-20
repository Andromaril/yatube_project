from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Create your views here.
# Главная страница
def index(request):
    """View - функция для главной страницы проекта."""

    posts = Post.objects.order_by('-pub_date')[:10]
    title_index = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title_index': title_index,
    }
    return render(request, 'posts/index.html', context)


# Страница со списком постов
def group_posts(request, slug):
    """View - функция для страницы с постами, отфильтрованными по группам."""

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title_group = 'Записи сообщества'
    context = {
        'group': group,
        'posts': posts,
        'title_group': title_group,

    }
    return render(request, 'posts/group_list.html', context)
