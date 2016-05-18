from django.shortcuts import render
from .models import Project, TeamMember

def get_index_page(request):
    return render(request, 'face/index.html', {
        'projects': Project.objects.all(),
        'team_members': TeamMember.objects.all(),
    })
