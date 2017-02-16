from django.db import models
from django.utils import timezone

class Post(models.Model):

	author = models.ForeignKey('auth.User') #vinculo con otro modelo
	title = models.CharField(max_length=200)#define texto con numero limitado de caracteres
	text = models.TextField()#textos largos sin un limite
	created_date = models.DateTimeField(default=timezone.now) #fecha y hora
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

# Create your models here.
