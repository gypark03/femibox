from django.contrib import admin
from femiLetter.models import Memos

# Register your models here.

class MemosAdmin(admin.ModelAdmin):
    list_display = ('title','author')

admin.site.register(Memos,MemosAdmin)
