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
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                            status='draft',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,)
    return render(request, 'blog/post/detail.html', {'post':post})
