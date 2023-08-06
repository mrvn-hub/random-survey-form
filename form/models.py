from django.db import models
from django.utils import timezone

# Create your models here.
class Form(models.Model):
	name = models.CharField("Full Name: ", max_length=25)
	agreement = models.BooleanField("Agreed", default=False)
	current_date = models.DateField("Session Date", default=timezone.now)
	current_time = models.TimeField("Session Time", default=timezone.now)

	def __str__(self):
		return self.name+" + "+self.current_date
	