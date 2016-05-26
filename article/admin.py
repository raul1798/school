from django.contrib import admin
from .models import Article, ArticleImage, ZnoDoc, Zno, Dpa, DpaDoc, Vchitel, VchitelDoc, Klassam, KlassamDoc

# Register your models here.
class ImageInline(admin.StackedInline):
     model = ArticleImage 
     extra = 3 

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ ImageInline, ]


class ZnoDocInline(admin.StackedInline):
     model = ZnoDoc 
     extra = 3 

class GalleryZno(admin.ModelAdmin):
    inlines = [ ZnoDocInline, ]


class DpaDocInline(admin.StackedInline):
     model = DpaDoc 
     extra = 3 

class GalleryDpa(admin.ModelAdmin):
    inlines = [ DpaDocInline, ]


class VchitelDocInline(admin.StackedInline):
     model = VchitelDoc 
     extra = 3 

class GalleryVchitel(admin.ModelAdmin):
    inlines = [ VchitelDocInline, ]


class KlassamDocInline(admin.StackedInline):
     model = KlassamDoc 
     extra = 3 

class GalleryKlassam(admin.ModelAdmin):
    inlines = [ KlassamDocInline, ]


admin.site.register(Article, GalleryAdmin)
admin.site.register(ArticleImage)
admin.site.register(ZnoDoc)
admin.site.register(Zno, GalleryZno)
admin.site.register(Dpa, GalleryDpa)
admin.site.register(DpaDoc)
admin.site.register(Vchitel, GalleryVchitel)
admin.site.register(VchitelDoc)
admin.site.register(Klassam, GalleryKlassam)
admin.site.register(KlassamDoc)