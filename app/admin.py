from django.contrib import admin
from .models import Yangiliklar,Image,Olimpiada,AboutSchool,Leadership,Yonalish,Category,YonalishImage
from unfold.admin import ModelAdmin
from parler.admin import TranslatableAdmin
class ImageInline(admin.TabularInline):
    model = Image

class YonalishImageInline(admin.TabularInline):
    model = YonalishImage

@admin.register(Yangiliklar)
class YangiliklarAdmin(TranslatableAdmin):
    inlines = [ImageInline]
    list_display = ('sarlavha', 'date', 'main_image')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

@admin.register(Olimpiada)
class OlimpiadaAdmin(ModelAdmin):
    list_display = ('Yil','Fan')

@admin.register(AboutSchool)
class SchooladaAdmin(ModelAdmin):
    list_display = ('Oquv_binolari','Pedagog_xodimlar','Oliy_va_birinchi_toifali_pedagoglar','Kompyuter_xonalari','Laboratoriya')

@admin.register(Leadership)
class LeadershipAdmin(ModelAdmin):
    list_display = ['Maktab_direktori']


@admin.register(Yonalish)
class YonalishAdmin(TranslatableAdmin):
    list_display = ('__str__', 'date', 'main_image')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',)
    