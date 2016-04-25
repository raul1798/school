from django.contrib import admin
from .models import Article, ArticleImage, ZnoDoc, Zno, History, HistoryImage, Dpa, DpaDoc, Vchitel, VchitelDoc

# Register your models here.
# class ChoiceInline(admin.StackedInline):
#     model = Image 
#     extra = 5 


admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(ZnoDoc)
admin.site.register(Zno)
admin.site.register(History)
admin.site.register(HistoryImage)
admin.site.register(Dpa)
admin.site.register(DpaDoc)
admin.site.register(Vchitel)
admin.site.register(VchitelDoc)