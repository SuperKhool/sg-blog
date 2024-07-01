from django.shortcuts import render,HttpResponse ,redirect ,get_object_or_404
from .models import *
from . import models
from django.db.models import Q

def post_by_category(req,category_id):
    #fetch the POST  from category_id
    post=Blog.objects.filter(status="Published",category_id=category_id)

    # try:
    #     categorys=category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    categorys=get_object_or_404(category,id=category_id)
        
    context={
        'post':post,
        'categorys':categorys,
    }
    return render(req,'post_by_category.html',context)




def blogs(request,slug):
    single_post=get_object_or_404(Blog,slug=slug,status='Published',)
    context={
        'single_post':single_post,
    }
    
    return render (request,'single_blog_page.html',context)


def search (request):
    keyword=request.GET.get('keyword')
    post=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status="Published")
    context={
        'post':post,
        'keyword':keyword
    }
    return render(request,'search.html',context)

