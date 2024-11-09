from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'msg', 'msg_date_time']