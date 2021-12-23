from django.forms import ModelForm

from . models import ProjectLanguage

#model form to add new repo
class Repository(ModelForm):
    class Meta:
        model = ProjectLanguage
        fields = '__all__'
