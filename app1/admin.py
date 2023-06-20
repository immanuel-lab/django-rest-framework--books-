from django.contrib import admin
from .models import Book,user,items,profile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# used to import export
class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
# admin.site.register(Book,BookAdmin)



admin.site.register(user)
# admin.site.register(items)
admin.site.register(profile)