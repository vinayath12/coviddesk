from django.contrib import admin
from .models import Place
# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Place,PlaceAdmin)
