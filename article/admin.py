from django.contrib import admin
from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)
#Admin panelini özelleştirmek için.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    #üstteki admin registerı sınıfla bağlamak için Meta işlemini yaptık.
    class Meta:
        model = Article
        