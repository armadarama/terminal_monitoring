from django.db import models
from terminal_monitoring.globalstrings import Globalstrings
from django.utils import timezone


class Terminal(models.Model):
	gs = Globalstrings()
	serial_number = models.IntegerField(null=False, blank=False)
	production_date = models.DateField(default=timezone.now, null=False, blank=True)
	sim_card_number = models.CharField(max_length=20, default="", null=False, blank=False)
	status = models.CharField(max_length=1,
		choices=(('A', gs.online),
			('B', gs.offline5lower),
			('C', gs.offline5greater),), 
		default='A', null=False, blank=False)
	accesspoint = models.ForeignKey('Accesspoint', on_delete=models.CASCADE, null=True, blank=True) #related_name = 'employees'

	def __str__(self):
		return str(self.serial_number)