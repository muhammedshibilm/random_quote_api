from django.contrib import admin
from .models import RandomData



@admin.register(RandomData)
class RandomDataAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'image_url']
