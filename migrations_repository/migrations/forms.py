from django import forms
from django.contrib.auth.models import User

from .models import Plan, Circuit

class PlanForm (forms.ModelForm) :

	class Meta :
		
		model = Plan
		fields = ['plan_number', 'plan_type']

class CircuitForm (forms.ModelForm) :

	class Meta :
	
		models = Circuit
		fields = ['cut_date', 'cut_lec', 'cmc_ticket', 'cut_file']

class UserForm (forms.ModelForm) :

	class Meta :
		
		model = User
		fields = ['username', 'email', 'password']


