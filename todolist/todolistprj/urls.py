from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TaskUpdate, TaskDelete, UserLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('task-create/', TodoCreate.as_view(), name='task-create'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')
]