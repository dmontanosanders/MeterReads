from django.db import models

# Create your models here.
class MetType(models.Model):
	mettype = models.CharField(max_length=30)
	def __unicode__(self):
		return self.mettype
