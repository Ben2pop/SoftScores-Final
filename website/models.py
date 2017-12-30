from django.db import models
from registration.models import MyUser

from django.core.urlresolvers import reverse

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100, default = '')
    team_hr_admin = models.ForeignKey(MyUser, blank=True, null=True)
    members = models.ManyToManyField(MyUser, related_name="members")

    def __str__(self):
        return self.team_name


class Project(models.Model):
    name = models.CharField(max_length=250)
    team_id = models.ForeignKey(Team, blank=True, null=True)
    project_hr_admin = models.ForeignKey('registration.MyUser', blank=True, null=True)
    candidat_answers = models.ManyToManyField('survey.response')

    def get_absolute_url(self):
        return reverse('website:ProjectDetails', kwargs = {'pk1' : self.pk})

    def __str__(self):
        return self.name