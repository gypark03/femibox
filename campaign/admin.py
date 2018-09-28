from django.contrib import admin
from campaign.models import Cam

# Register your models here.

class CamAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Cam,CamAdmin)
