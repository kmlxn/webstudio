from django.contrib import admin
from .models import Project, TeamMember, CustomerMessage, DevelopmentStage, Service
from modeltranslation.admin import TranslationAdmin


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'picture', 'description', 'snippet']
            }
        )
    ]
    list_display = ('name',)


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
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

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(DevelopmentStage)
class DevelopmentStageAdmin(TranslationAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'text', 'picture']
            }
        )
    ]
    list_display = ('name',)


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'description', 'snippet', 'html_tag_for_picture']
            }
        )
    ]
    list_display = ('name',)
