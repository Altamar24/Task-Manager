from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    """Класс для получения списка всех задач авторизованного пользователя"""

    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.request.user.tasks.all()


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания задачи, передается модель Task

    Attributes
    ----------
    title : CharField
        название задачи
    description : TextField
        описание задачи
    priority : SmallIntegerField
        приоритет задачи
    due_data : DateTimeField
        срок исполнения задачи
    completed : BooleanField
        галочка для отметки исполнения
     Methods
    -------
    form_valid()
        метод устанавливает пользователя, который отправил форму, в качестве
        владельца объекта, и затем продолжает стандартную обработку формы.
    """

    model = Task
    fields = ('title', 'description', 'priority', 'due_data', 'completed')
    template_name = 'tasks/add_tasks.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """form.instance - это экземпляр модели, который будет сохранён при
        отправке формы.

        self.request.user - это объект пользователя, который совершил запрос.
        В данном случае, мы устанавливаем пользователя, который отправил форму,
        в качестве владельца экземпляра модели.

        return super().form_valid(form) - это вызов метода form_valid базового
        класса, который продолжит обработку формы.
        """

        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для изменения задачи, передается модель Task

    Attributes
    ----------
    title : CharField
        название задачи
    description : TextField
        описание задачи
    priority : SmallIntegerField
        приоритет задачи
    due_data : DateTimeField
        срок исполнения задачи
    completed : BooleanField
        галочка для отметки исполнения
    """

    model = Task
    fields = ('title', 'description', 'priority', 'due_data', 'completed')
    template_name_suffix = "s_update"
    success_url = reverse_lazy('index')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления задачи, передается модель Task

    Methods
    -------
    get_object()
        метод позволяет удалять задачу только автору этой задачи
    """
    model = Task
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        """super(TaskDeleteView, self).get_object(queryset) - вызывает метод 
        get_object базового класса для получения объекта задачи, который 
        должен быть удалён.

        if Task.owner != self.request.user: - проверяет, является ли текущий 
        пользователь (self.request.user) владельцем задачи (Task.owner).

        raise Http404("Вы не можете удалить данную задачу") - вызывается 
        исключение Http404, которое приводит к отображению страницы 404 с 
        сообщением, что пользователь не может удалить задачу.

        return Task - если проверка пройдена, метод возвращает объект задачи 
        для дальнейшего удаления.
        """

        Task = super(TaskDeleteView, self).get_object(queryset)
        if Task.owner != self.request.user:
            raise Http404("Вы не можете удалить данную категорию")
        return Task
