from django.db import models


class Site(models.Model):
	name = models.CharField(max_length=100, default ="", null=False, blank=False)
	location = models.CharField(max_length=100, default ="", null=False, blank=False)

	def __str__(self):
		return self.name + ' - ' + self.location