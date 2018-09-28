from django.contrib import admin
from question.models import QAA, FAQ

# Register your models here.

class QAAAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')


admin.site.register(QAA, QAAAdmin)
admin.site.register(FAQ, FAQAdmin)
