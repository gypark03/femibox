from django.contrib import admin
from notice.models import notice

# Register your models here.

class noticeAdmin(admin.ModelAdmin):
    list_display = ('title',  'create_date')
    list_filter = ('create_date',)
    search_fields = ('title', 'content')

admin.site.register(notice, noticeAdmin)
