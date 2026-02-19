from django.contrib import admin
from .models import Post   
from django.db import models
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'updated_at')
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}  # cel --> źródło slug będzie generowany na podstawie title
    show_facets = admin.ShowFacets.ALWAYS
    