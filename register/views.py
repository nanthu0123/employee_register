from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

def employee_form(request):
    if request.method=='GET':
        context={'form':EmployeeForm()}
        return render(request,'register/employee_form.html',context)
    else:
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')

def employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,'register/employee_list.html',context)

def employee_delete(request):
    return