from django.contrib import admin

# Register your models here.

from .models import Post,Category,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)


