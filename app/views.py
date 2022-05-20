from multiprocessing import context
from django.shortcuts import render
from app.models import Todo
from app.forms import TodoForm

# Create your views here.
def index(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
    "form":form
            }
    return render(request,'index.html',form)
