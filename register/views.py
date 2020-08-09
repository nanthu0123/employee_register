from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

def employee_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form=EmployeeForm()
            context={'form':form}
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
            context={'form':form}
        return render(request,'register/employee_form.html',context)
    else:
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('list')

def employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,'register/employee_list.html',context)

def employee_delete(request):
    return