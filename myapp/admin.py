from django.contrib import admin
from .models import User, Item

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'gender')
    search_fields = ('username', 'email', 'first_name', 'last_name')   
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at', 'user')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')