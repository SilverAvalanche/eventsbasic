# models.py- Organizaton

from django.db import models
from apps.eventmanager.season.models import * # imports all?

class Organization(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    deleted = models.BooleanField(default=False, db_index=True)
    organizationSeasons= models.ManyToManyField(Season, through='OrganizationSeason', 
                                                through_fields=('organization', 'season'))
    @property
    def delete(self):
        self.deleted = True
        self.save()



class OrganizationSeason(models.Model):
    season = models.ForeignKey(Season)
    organization = models.ForeignKey(Organization)


