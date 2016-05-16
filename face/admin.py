from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'picture', 'description']
            }
        )
    ]
    list_display = ('name',)
