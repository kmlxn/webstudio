from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField()
    description = models.TextField(null=True)

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


class DevelopmentStage(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField()
