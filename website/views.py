from django.shortcuts import render

from .models import Portfolio

def home(request):
    projects = Portfolio.objects.all()
    return render(request, 'website/index.html',{'projects': projects})

def about(request):
    return render(request, 'website/about.html')

def services(request):
    return render(request, 'website/services.html')



def base(request):
    return render(request, 'website/base.html')



def portfolio(request):
    projects = Portfolio.objects.all()
    return render(request, 'website/portfolio.html', {'projects': projects})


from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

from django.shortcuts import render, get_object_or_404
from .models import Service

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    other_services = Service.objects.exclude(id=service.id)[:5]  # Show 5 other services
    return render(request, 'service_detail.html', {'service': service, 'other_services': other_services})

