from django.db import models


class TaskModel(models.Model):
	STATUS_CHOICES = (
		('td', 'to-do'),
		('ip', 'in-process'), 
		('f', 'finished'), 
	)
	title = models.CharField(max_length=64)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='td')
	create = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.title} - {self.status}'


	class Meta:
		ordering = ['-create', ]
 