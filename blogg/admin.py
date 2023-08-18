from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import *


class Admin(admin.ModelAdmin):
     list_display=("username","password","Password confirmation")
    # prepopulated_fields = {"slug": ("username", "password" "Password confirmation",)}

class CommentAdmin(admin.ModelAdmin):
    list_display =('name','email','body','created_on','active')
    list_filter =('active','created_on')
    search_fields=('name','email','body')
    #actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)

class PostAdmin(admin.ModelAdmin):
    def Image_tag(self,obj):
        return format_html('<img src="{}" style="height:50px; width:50px;"/>'.format(obj.Image.url))
    
    search_fields = ('title',)
    list_display = ('title','Image_tag','create_date','published_date','text')
    list_filter = ["published_date"]

        

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    list_filter = ["title"]

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ["name"]
    



    
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)
