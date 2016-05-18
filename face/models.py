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
