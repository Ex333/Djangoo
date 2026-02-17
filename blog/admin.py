from django.contrib import admin
from .models import Post   
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}  # cel --> źródło slug będzie generowany na podstawie title