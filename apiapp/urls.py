from django.urls import path
from . import views

urlpatterns = [
    path('',views.apioverview, name= "api-overview"),
    path('tasklist/',views.TaskList, name= "task-list"),
    path('taskdetail/<str:pk>/',views.TaskDetail, name= "task-detail"),
    path('taskcreate/',views.TaskCreate, name= "task-create"),
    path('taskupdate/<str:pk>/',views.TaskUpdate, name= "task-update"),
     path('taskdelete/<str:pk>/',views.TaskDelete, name= "task-delete"),

]