from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# class Admin(admin.ModelAdmin):
#     list_display=("username","password","Password confirmation",)
    # prepopulated_fields = {"slug": ("username", "password" "Password confirmation",)}

    
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User, UserAdmin)
