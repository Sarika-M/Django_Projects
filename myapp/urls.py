from django.urls import path
from .views import employee_list, employee_create, employee_edit, employee_delete,home,employee_edits

urlpatterns = [
    path('', home, name='home'),
    path('employee_list/', employee_list, name='employee_list'),
    path('employee_edits/', employee_edits, name='employee_edits'),
    path('create/', employee_create, name='employee_create'),
    path('edit/<int:pk>/', employee_edit, name='employee_edit'),
    path('<int:pk>/delete/', employee_delete, name='employee_delete'),
]
