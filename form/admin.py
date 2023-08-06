from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
	list_display = ("name", "agreement", "current_date", "current_time")

admin.site.register(Form, FormAdmin)