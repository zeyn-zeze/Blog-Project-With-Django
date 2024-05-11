from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAmin(admin.ModelAdmin):
    list_display = ["title","author","create_date"]
    list_display_links = ["title","author","create_date"]
    search_fields = ["title"]
    list_filter = ["create_date"]
    class Meta : 
       model=Article