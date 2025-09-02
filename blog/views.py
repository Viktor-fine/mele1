from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


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
    women = ['Анжелина Джоли', 'Дженифер Лоуренс', 'Джулия Робертс', 'Марго Робби', 'Ума Турман', 'Ариана Гранде', 'Савичева']
    p = Paginator(women, 3)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    name = 'Виктор'
    q = 80
    context = {'parametr': q, 'name': name }
    return render(request, 'blog/post/page.html', context)
