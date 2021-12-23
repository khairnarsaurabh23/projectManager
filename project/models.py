from django.db import models
from datetime import datetime

#language in which project id developed
class ProjectLanguage(models.Model):
	language_category = models.CharField(max_length=100)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=50)

	class Meta:
		#for django plurals
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.language_category

#hold code
class Project(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	published = models.DateTimeField("date published", default=datetime.now() )

	series = models.ForeignKey(ProjectLanguage, default=1, verbose_name="Projects", on_delete=models.SET_DEFAULT )
	slug = models.CharField(max_length=50, default=1)

	def __str__(self):
		return self.title