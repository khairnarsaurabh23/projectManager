from django.forms import ModelForm, PasswordInput

from . models import User

#registration form
class register(ModelForm):
	class Meta:
		model = User
		fields = 'username', 'email', 'password'
		widgets = {
			'password':PasswordInput()
		}
