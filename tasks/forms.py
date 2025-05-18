from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'w-full p-2 border border-gray-300 rounded',
            }
        )
    )

    class Meta:
        model = Tasks
        fields = ['title', 'description', 'due_date', 'priority', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Enter task title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Enter task description',
                'rows': 4,
            }),
            'priority': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'mr-2',
            }),
        }
