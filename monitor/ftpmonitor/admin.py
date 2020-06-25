from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
class Files_admin_inline(admin.TabularInline):
	model=Files
	fields=('file_name','file_date')
	readonly_fields=['file_date','file_time']
admin.site.register(
		Folder,
		DraggableMPTTAdmin,
		list_display=('tree_actions','indented_title','id','level','name','folder_date'),
		search_fields =('name','folder_date'),
		list_display_links=('indented_title',),
		inlines=[Files_admin_inline]
	)

# Register your models here.
#admin.site.register(Folder)
admin.site.register(Files)
admin.site.register(auth)
