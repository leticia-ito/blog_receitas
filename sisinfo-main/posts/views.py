from django.http import HttpResponseRedirect
from .temp_data import post_data
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Receita


def list_posts(request):
    post_list = Receita.objects.all()
    context = {"post_list": post_list}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Receita, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Receita.objects.filter(ingred__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

def create_post(request):
    if request.method == 'POST':
        post_title = request.POST['title']
        post_ingred = request.POST['ingred']
        post_mdf = request.POST['mdf']
        post = Receita(title=post_title,
                      ingred=post_ingred,
                      mdf=post_mdf)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})
    
def update_post(request, post_id):
    post = get_object_or_404(Receita, pk=post_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.ingred = request.POST['ingred']
        post.mdf = request.POST['mdf']
        post.save()
        return HttpResponseRedirect(reverse("posts:detail", args=(post.id, )))
    context = {'post': post}
    return render(request, 'posts/update.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Receita, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))
    context = {'post': post}
    return render(request, 'posts/delete.html', context)
