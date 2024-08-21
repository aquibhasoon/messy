from django.contrib import admin
from .models import Messcut

# Register your models here.

@admin.register(Messcut)
class MesscutAdmin(admin.ModelAdmin):
	list_display = ['start_date','end_date']
	list_filter = ['start_date','end_date']
	search_fields = ['start_date','end_date']
	list_per_page = 10