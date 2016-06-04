from django.contrib import admin
from .models import Project, TeamMember, CustomerMessage, DevelopmentStage, Service, ProgrammingLanguage, ProgrammingFramework, ProgrammingTool
from modeltranslation.admin import TranslationAdmin


class ProgrammingLanguageInLine(admin.TabularInline):
    model = ProgrammingLanguage.services.through
    extra = 3


class ProgrammingFrameworkInLine(admin.TabularInline):
    model = ProgrammingFramework.services.through
    extra = 3


class ProgrammingToolInLine(admin.TabularInline):
    model = ProgrammingTool.services.through
    extra = 3


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
    inlines = [ProgrammingLanguageInLine, ProgrammingFrameworkInLine, ProgrammingToolInLine]



@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'image']
            }
        )
    ]
    inlines = [ProgrammingLanguageInLine]
    exclude = ('services',)


@admin.register(ProgrammingFramework)
class ProgrammingFrameworkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'image']
            }
        )
    ]
    inlines = [ProgrammingFrameworkInLine]
    exclude = ('services',)


@admin.register(ProgrammingTool)
class ProgrammingToolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['name', 'image']
            }
        )
    ]
    inlines = [ProgrammingToolInLine]
    exclude = ('services',)
