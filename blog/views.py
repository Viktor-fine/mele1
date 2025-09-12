from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.models import User


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3) # по 3 статьи на странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page':page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                            status='draft',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,)
    return render(request, 'blog/post/detail.html', {'post':post})

def num_page(request):
    women = ['Анжелина Джоли', 'Дженифер Лоуренс', 'Джулия Робертс', 'Марго Робби', 'Ума Турман', 'Ариана Гранде', 'Савичева', 'А-студио']
    p = Paginator(women, 3)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'blog/post/page.html', {'page_obj': page_obj, 'page_num': page_number})

def pages(request):
    women = ['Анжелина Джоли', 'Дженифер Лоуренс', 'Джулия Робертс',
            'Марго Робби', 'Ума Турман', 'Ариана Гранде',
            'Савичева', 'А-студио', 'Чеботина',
            'Орбакайте', 'Королёва', 'Салтыкова',
            'Варум', 'Олегрова', 'Бабкина',
            'Мия Бойко', 'Капустина',]
    paginator = Paginator(women, 3)
    a = paginator.num_pages
    return render(request, 'blog/post/pagina.html', {'a': a})
