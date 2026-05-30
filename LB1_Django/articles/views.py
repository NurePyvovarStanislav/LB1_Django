from django.shortcuts import render, redirect, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by("-publication_date")
    return render(request, "articles/article_list.html", {"articles": articles})


def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect("article_list")

    return render(request, "articles/article_form.html", {"article": article})


def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article.delete()
        return redirect("article_list")

    return render(request, "articles/article_confirm_delete.html", {"article": article})