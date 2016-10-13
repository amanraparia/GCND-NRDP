from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.

class Plan (models.Model) :

	user = models.ForeignKey (User, default = 1)
	plan_number = models.CharField (max_length = 15)
	plan_type = models.CharField (max_length = 20)

	def __str__ (self) :
	
		return self.plan_number + '-' +  self.plan_type

class Circuit (models.Model) :

	plan = models.ForeignKey (Plan, on_delete = models.CASCADE)
	cut_date = models.DateTimeField ('migration date')
	cut_lec = models.CharField (max_length = 20)
	cmc_ticket = models.IntegerField ()
	cut_file = models. FileField ('')

	def __str__ (self) :
	
		return self.cut_date + '-' + self.cmc_ticket


	
