from django.contrib import admin
from .models import Project, TeamMember


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


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'picture', 'role']
            }
        )
    ]
    list_display = ('name',)
