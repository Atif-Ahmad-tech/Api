from django.contrib import admin
from .models import Menuitem, catagory
# Register your models here.
class catagoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':    ('title',)}
admin.site.register(Menuitem)
admin.site.register(catagory, catagoryAdmin)