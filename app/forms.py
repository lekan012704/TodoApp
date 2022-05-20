from socket import form
from app.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
     model = Todo
     fields = ("item")