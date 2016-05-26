from modeltranslation.translator import register, TranslationOptions
from .models import Project, TeamMember, DevelopmentStage


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'role',)


@register(DevelopmentStage)
class DevelopmentStageTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)
