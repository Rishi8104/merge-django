from django.contrib import admin

# Register your models here.
from.models import Question,Choice

# class QuestionAdmin(admin.ModelAdmin):
#        fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#        ]
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text","slug"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display =("question_text","pub_date","slug")
    inlines = [ChoiceInline]
    
    # prepopulated_fields={"slug":("question_text",)}
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
