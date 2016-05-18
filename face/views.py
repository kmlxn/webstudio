from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, TeamMember, CustomerMessage


def get_index_page(request):
    if request.method == 'POST':
        CustomerMessage.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        return HttpResponse('ok')
    else:
        return render(request, 'face/index.html', {
            'projects': Project.objects.all(),
            'team_members': TeamMember.objects.all(),
        })
