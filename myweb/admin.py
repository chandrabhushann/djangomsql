from django.contrib import admin
from .models import ART, VID, VIDEO, MUS
# Register your models here.

class ARTAdmin(admin.ModelAdmin):
    search_fields = ('title',)

class VIDAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class VIDEOdmin(admin.ModelAdmin):
    search_fields = ('title',)

class MUSAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.register(ART, ARTAdmin)
admin.site.register(VID, VIDAdmin)
admin.site.register(VIDEO, VIDEOdmin)
admin.site.register(MUS, MUSAdmin)

