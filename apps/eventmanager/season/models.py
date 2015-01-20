#models.py- Season

from django.db import models
from apps.eventmanager.team.models import * # Contains classes Team, TeamRegistrant(Thru Table)

# Season is for a period of time like a football season or a specific event like a weekend convention
class Season(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(auto_now=True)
    
    deleted = models.BooleanField(default=False, db_index=True)
    #datetimefield format ['%Y-%m-%d %H:%M']
    
    seasonTeams = models.ManyToManyField(Team, through='SeasonTeam', through_fields=('season','team')) 
    
    @property
    def delete(self):
        self.deleted = True
        self.save()
      
    
     
class SeasonTeam(models.Model):
    season = models.ForeignKey(Season)
    team = models.ForeignKey(Team)

    
    
     
