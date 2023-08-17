from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# class Admin(admin.ModelAdmin):
#     list_display=("username","password","Password confirmation",)
    # prepopulated_fields = {"slug": ("username", "password" "Password confirmation",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =('name','email','body','created_on','active')
    list_filter =('active','created_on')
    search_fields=('name','email','body')
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)
        

    
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User, UserAdmin)
