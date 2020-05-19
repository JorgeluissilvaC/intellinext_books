from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registroFormUser(UserCreationForm):
    class Meta:
        model = User 
        fields = [  
                    'username',
                    'first_name', 
                    'last_name',
                ]
        labels = {
                    'username': 'Usuario',
                    'first_name': 'Nombre',
                    'last_name': 'Apellido',
        }
