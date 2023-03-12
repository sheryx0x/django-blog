from django.db import models

class post(models.Model):
	title = models.CharField(max_length=200, null=True)
	author = models.CharField(max_length=200, null=True)
	body = models.TextField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

    
def __str__(self):																									
	    return self.title
