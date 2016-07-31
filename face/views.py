import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Project, TeamMember, CustomerMessage, DevelopmentStage, Service


def get_index_page(request):
	if request.method == 'POST':
		message = CustomerMessage.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			phone=request.POST['phone'],
			message=request.POST['message'],
		)
		notificate_team_about_new_message(message)
		return HttpResponse('ok')
	else:
		return render(request, 'face/index.html', {
			'projects': Project.objects.all(),
			'team_members': TeamMember.objects.all(),
			'development_stages': DevelopmentStage.objects.all(),
			'services': Service.objects.all(),
			'year': datetime.datetime.now().year
		})

def notificate_team_about_new_message(message):
	subject = 'Kirapps - новое сообщение'
	message_template = 'Имя: {name}\nEmail: {email}\nPhone: {phone}\n' + \
		'Message: {message}\nTime sent: {time_sent}'
	message = message_template.format(
		name=message.name,
		email=message.email,
		phone=message.phone,
		message=message.message,
		time_sent=message.time_sent
	)

	send_mail(subject, message, settings.EMAIL_HOST_USER,
		settings.EMAIL_SEND_TO, fail_silently=False)
