from django.contrib import admin
from .models import Thing
# Register your models here.

@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for teams."""
    
    list_display = [
        'name', 'description', 'quantity', 'created_at'
    ]
