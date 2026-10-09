from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, TaskForm
from .models import Task


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
    else:
        form = RegisterForm()

    return render(request, "tasks/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("task_list")
    else:
        form = AuthenticationForm(request)

    return render(request, "tasks/login.html", {"form": form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "tasks/task_list.html", {
        "tasks": tasks
    })


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {
        "form": form,
        "page_title": "Create Task"
    })


@login_required
def task_edit(request, pk):
    task = get_object_or_404(
        Task, pk=pk, user=request.user
    )

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {
        "form": form,
        "page_title": "Edit Task"
    })


@login_required
def task_delete(request, pk):
    task = get_object_or_404(
        Task, pk=pk, user=request.user
    )

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request, "tasks/task_confirm_delete.html", {
        "task": task
    })