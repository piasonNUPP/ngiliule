from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .forms import DimoForm, TaskForm, UpdateForm
from .models import Dimo, Task
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm






class StudentListView(ListView):
    model = Dimo
    template_name = 'list/dimo_list.html'
    context_object_name = 'students'
    paginated_by = 4

    def get_queryset(self):
        return Dimo.objects.order_by('-id')


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Dimo
    template_name = 'list/add.html'
    form_class = DimoForm
    success_url = reverse_lazy('slist')
    success_message = "Data Added Successfully"


class StudentDetailView(DetailView):
    model = Dimo
    template_name = 'list/dimo_detail.html'

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Dimo
    template_name = 'list/edit.html'
    form_class = DimoForm
    success_url = reverse_lazy('slist')
    success_message = "Data Updated Successfully"


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Dimo
    template_name = 'list/delete.html'
    
    success_url = reverse_lazy('slist')
    success_message = "Data Deleted Successfully"


def ListTask(request):
    queryset = Task.objects.order_by('complete', 'due')
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks':queryset,
        'form':form
    }
    return render(request, 'list/home.html', context)

def UpdateTask(request, pk):
    queryset = Task.objects.get(id = pk)
    form = UpdateForm(instance=queryset)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        
        'form':form
    }
    return render(request, 'list/update_task.html', context)

def DeleteTask(request, pk):
    queryset = Task.objects.get(id = pk)
    
    if request.method == "POST":
       queryset.delete()
       return redirect('/')

    context = {
        
        'item':queryset
    }
    return render(request, 'list/delete_task.html', context)