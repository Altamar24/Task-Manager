from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse

from .models import Task


class TaskListView(ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.request.user.tasks.all()


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'tasks/add_tasks.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title', 'description', 'priority', 'due_data', 'completed')
    template_name_suffix = "s_update"
    success_url = reverse_lazy('index')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        Task = super(TaskDeleteView, self).get_object(queryset)
        if Task.owner != self.request.user:
            raise Http404("Вы не можете удалить данную категорию")
        return Task
