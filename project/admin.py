from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from . models import ProjectLanguage, Project


class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		("title/Date", {"fields": ["title", "published"]}),
		("URL", {"fields": ["slug"]}),
		("Series", {"fields":["series"]}),
		("Content", {"fields": ["content"]}),
	]

	#overrides the TextField to give a full editor using the TinyMCE
	formfield_overrides = {
		models.TextField: {TinyMCE()}
	}


admin.site.register(ProjectLanguage)
admin.site.register(Project)


