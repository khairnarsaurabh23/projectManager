from django.shortcuts import render

from . forms import Repository
from . models import ProjectLanguage

#function to add new repo to the web-site
def add_repository(request):
    return render(request,
                    "project/repository.html",
                    form=Repository
                )
