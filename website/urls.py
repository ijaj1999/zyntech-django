from django.urls import path
from . import views  # Import views

from django.urls import path
from .views import blog_list, blog_detail

from .views import services, service_detail

urlpatterns = [

]

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('about/', views.about, name='about'),  # About Page
    #path('services/', views.services, name='services'),  # Services Page
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio Page
    path('base/', views.base, name='base'),  # base Page

    path('blog/', blog_list, name='blog_list'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),

    path('services/', services, name='services'),
    path('services/<slug:slug>/', service_detail, name='service_detail'),   
    
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
