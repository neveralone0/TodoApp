from django.contrib import admin
from todo_app.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'status', )
	ordering = ['-create', ]
	search_fields = ['title', 'status', ]
	

admin.site.register(TaskModel, TaskAdmin)
