from django.db import models


class Accesspoint(models.Model):
	name = models.CharField(max_length=100)
	ip_adress = models.CharField(max_length=50)
	#site = models.ForeignKey(Site, on_delete=models.CASCADE)