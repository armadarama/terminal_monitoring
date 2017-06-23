from django.db import models


class Accesspoint(models.Model):
	name = models.CharField(max_length=100, default ="", null=False, blank=False)
	ip_adress = models.CharField(max_length=50, default ="", null=False, blank=False)
	site = models.ForeignKey('Site', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.name