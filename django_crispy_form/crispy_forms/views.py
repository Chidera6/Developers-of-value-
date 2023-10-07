from django.shortcuts import render
from .forms import TodosForm
 
def todo_view(request):
    context ={}
    form = TodosForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "crispy_forms/todo.html", context)