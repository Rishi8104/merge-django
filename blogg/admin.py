from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Category
from .models import Tag

class Admin(admin.ModelAdmin):
    list_display=("username","password","Password confirmation",)
    # prepopulated_fields = {"slug": ("username", "password" "Password confirmation",)}

    
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)