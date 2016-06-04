from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField()
    description = models.TextField(null=True)
    snippet = models.TextField(null=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField()
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CustomerMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DevelopmentStage(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    snippet = models.TextField()
    html_tag_for_picture = models.TextField()

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='programming')
    services = models.ManyToManyField(Service, related_name='programming_languages')

    def __str__(self):
        return self.name


class ProgrammingFramework(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='programming')
    services = models.ManyToManyField(Service, related_name='programming_frameworks')

    def __str__(self):
        return self.name


class ProgrammingTool(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='programming')
    services = models.ManyToManyField(Service, related_name='programming_tools')

    def __str__(self):
        return self.name
