from django.db import models


class Terminal(models.Model):
	serial_number = models.IntegerField()
	production_date = models.CharField(max_length=15)
	sim_card_number = models.CharField(max_length=20)
	#status = models.CharField(max_length=1,
	#	choices=(('A', gs.online),
	#		('B', gs.offline5lower),
	#		('C', gs.offline5greater),), 
	#	default='A', null=False, blank=False)
	#accesspoint = models.ForeignKey(Accesspoint, on_delete=models.CASCADE)