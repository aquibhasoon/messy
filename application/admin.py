from django.contrib import admin

# Register your models here.
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	list_display = ['applicant','mess_no','accepted','created_at']
	list_filter = ['applicant','hostel','mess_no','accepted','created_at']
	search_fields = ['applicant','hostel','accepted','created_at']
	list_per_page = 10
