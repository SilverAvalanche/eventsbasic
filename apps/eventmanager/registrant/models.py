# models.py- Registrant

from django.db import models
from apps.eventmanager.team.models import * #includes Team, TeamRegistrant (Thru table) 

#TODO PAYMENTS

class Registrant(models.Model):
    fName = models.CharField(max_length=100, default='John')
    lName = models.CharField(max_length=100, default='Doe')
    email = models.EmailField(max_length=100, default='example@example.com')
    
    deleted = models.BooleanField(default=False, db_index=True)


    @property
    def delete(self):
        self.deleted = True
        self.save()

