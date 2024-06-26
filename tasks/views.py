from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.http import Http404

from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.request.user.tasks.all()


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('title', 'description', 'priority', 'due_data', 'completed')
    template_name = 'tasks/add_tasks.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('title', 'description', 'priority', 'due_data', 'completed')
    template_name_suffix = "s_update"
    success_url = reverse_lazy('index')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        Task = super(TaskDeleteView, self).get_object(queryset)
        if Task.owner != self.request.user:
            raise Http404("Вы не можете удалить данную категорию")
        return Task
