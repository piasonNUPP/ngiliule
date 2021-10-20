from .models import Dimo, Task
from django.forms import ModelForm
from django import forms


class DimoForm(ModelForm):


    class Meta:
        model = Dimo
        fields = ['fname', 'course', 'year', 'place']

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label = False,
        widget = forms.TextInput(attrs={'placeholder':'Task title'})
    )
    due = forms.CharField(
        label = False,
        widget = forms.TextInput(attrs={'placeholder':'Due date'})
    )
    dawa = forms.CharField(
        label = False,
        widget = forms.TextInput(attrs={'placeholder':'dawa'})
    )


    class Meta:
        model = Task
        fields = ['title', 'due', 'dawa']

class UpdateForm(forms.ModelForm):
    title = forms.CharField(
        label = False,
        widget = forms.TextInput(attrs={'placeholder':'Task title'})
    )


    class Meta:
        model = Task
        fields = ['title', 'due', 'dawa', 'complete']