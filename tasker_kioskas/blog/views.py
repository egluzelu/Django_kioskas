from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from . import models

def blog_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/blog_list.html', {
        'blog_list': models.Blog.objects.all(),
    })

def blog_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'blog/blog_detail.html', {
        'blog': get_object_or_404(models.Blog, pk=pk),
    })
