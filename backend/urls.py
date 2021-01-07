from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'backend'

urlpatterns = [
    path('', views.api_root, name='root'),
    path('set-csrf/', views.set_csrf_token, name='set-csrf-token'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('user/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
