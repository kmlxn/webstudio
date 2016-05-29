from modeltranslation.translator import register, TranslationOptions
from .models import Project, TeamMember, DevelopmentStage, Service


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'snippet')


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'role')


@register(DevelopmentStage)
class DevelopmentStageTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'snippet', 'programming_languages',
        'programming_frameworks', 'programming_tools')
