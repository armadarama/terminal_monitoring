from django.db import models


class Site(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)