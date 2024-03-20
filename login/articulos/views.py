from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article


def render_articulos(request):
    articulos = Article.objects.all()
    total_articulos = articulos.count()
    return render(request, 'articulos.html', {'articulos': articulos,'total_articulos': total_articulos})


def articleDetail(request, id):
    articulo = get_object_or_404(Article,pk = id)
    return render(request, 'article_detail.html', {'articulo':articulo})


@login_required
def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '¡Artículo agregado correctamente!')
            return redirect('home')  # Redirige a la página de inicio o a donde quieras
    else:
        form = ArticleForm()
    return render(request, 'agregar_articulo.html', {'form': form})