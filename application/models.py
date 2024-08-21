from django.db import models
from django.contrib.auth.models import User
from mess.models import *

# Create your models here.

hostels = [
	('Sagar', 'Sagar'),

]

class Application(models.Model):
	applicant = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	mess_no = models.IntegerField(default=100)
	hostel = models.CharField(max_length=100, choices=hostels)
	accepted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	messcuts = models.ManyToManyField(Messcut, blank=True)

	def __str__(self):
		return str(self.applicant.username + ' - ' + self.created_at.strftime('%d-%m-%Y'))


class AcceptedApplication(Application):
    class Meta:
        proxy = True