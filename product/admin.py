from django.contrib import admin
from product.models import box, goods

# Register your models here.

class BoxAdmin(admin.ModelAdmin):
    list_display = ('b_name',)
    search_filter = ('b_name', 'content')

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('g_name',)
    searcth_filter = ('g_name', 'content')

admin.site.register(box,BoxAdmin)
admin.site.register(goods,GoodsAdmin)
