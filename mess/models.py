from django.db import models

# Create your models here.

class Messcut(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return f"Messcut from {self.start_date} to {self.end_date}"