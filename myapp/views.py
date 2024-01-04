from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse

def home(request):
    return render(request,'myapp/home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'myapp/employee_list.html',{'employees': employees})

def employee_edits(request):
    employees = Employee.objects.all()
    return render(request, 'myapp/employee_edits.html',{'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'myapp/employee_form.html', {'form': form})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_edits')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'myapp/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_edits')
    return render(request, 'myapp/employee_confirm_delete.html', {'employee': employee})
