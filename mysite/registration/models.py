from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
	pass
	'''
		choices_objects = (
			('A', 'Agent'),
			('B', 'Customer')
		)
		user_choices = models.Charfield(max_length=1, choices=choices_objects)
		first_name = models.Charfield(max_length=50)
		last_name = models.Charfield(max_length=50)
	'''
