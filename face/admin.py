from django.contrib import admin
from .models import Project, TeamMember, CustomerMessage


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


@admin.register(CustomerMessage)
class CustomerMessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'email', 'phone', 'message', 'time_sent']
            }
        )
    ]
    readonly_fields = CustomerMessage._meta.get_all_field_names()
    list_display = ('name', 'time_sent')
