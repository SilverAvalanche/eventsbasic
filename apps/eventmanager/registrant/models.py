# models.py- Registrant
from django.contrib.auth.models import User
from django.db import models
from apps.eventmanager.team.models import * #includes Team, TeamRegistrant (Thru table) 
#TODO PAYMENTS

class Registrant(models.Model):
    fName = models.CharField(max_length=100, default='John')
    lName = models.CharField(max_length=100, default='Doe')
    email = models.EmailField(max_length=100, default='example@example.com')
    created = models.DateTimeField(auto_now=True, auto_now_add=True )        
    deleted = models.BooleanField(default=False, db_index=True)
    # point to the user model?

    @property
    def delete(self):
        self.deleted = True
        self.save()
    
    def is_active(self):
        if (self.deleted == False):
            return True
        return False
    def get_payments(self):
        return self.payment_set.all()
        
