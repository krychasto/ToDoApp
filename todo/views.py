from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todo.models import Todo
import schedule
import time

def job():
	print("hello world")
	schedule.every(2).seconds.do(job)

def razmor(request):
	return HttpResponse("Hello World")

def home(request):
	todo_items = Todo.objects.all().order_by("-added_date")
	return render(request, "todo/index.html", {
		"todo_items": todo_items
	})

@csrf_exempt
def add_todo(request):
	now = timezone.now()
	content = request.POST["content"]
	created_obj = Todo.objects.create(added_date=now, text=content)
	return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
	Todo.objects.get(id=todo_id).delete()
	return HttpResponseRedirect("/")
