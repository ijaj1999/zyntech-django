from django.contrib import admin

# Register your models here.
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {"slug": ("title",)}


from django.contrib import admin
from .models import Portfolio

admin.site.register(Portfolio)


from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}