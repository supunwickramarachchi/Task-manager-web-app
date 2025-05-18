from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tasks
from .forms import TaskForm
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.db.models import Q

class TaskListView(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'
    
    def get_queryset(self):
        queryset = Tasks.objects.filter(user=self.request.user).order_by('completed', 'due_date')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(priority__icontains=query)
            )
        return queryset
        
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')
    
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
    
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
        
class TaskToggleView(LoginRequiredMixin, View):
    @method_decorator(require_POST)
    def post(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')