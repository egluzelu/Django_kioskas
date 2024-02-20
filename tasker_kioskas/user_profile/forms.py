from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text=_('''
            Your password can not be too similar to your other personal information,<br> 
            Your password must contain at least 8 characters,<br> 
            Your password can not be a commonly used,<br>
            Your password can not be entirely numeric.''')
