from django.shortcuts import render, HttpResponse
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context ={
        'emps': emps

    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept =int(request.POST['dept'])
        role = int(request.POST['role'])
        email = request.POST['email']
        new_emp = Employee(first_name=first_name, last_name= last_name, salary= salary, bonus= bonus, phone=phone,dept_id= dept, role_id=role, email=email,  hiring_date= datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse(status=405)



def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please enter A valid EMP ID")
    emps= Employee.objects.all()
    context ={
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)



def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if first_name:
            emps = emps.filter(first_name__icontains = first_name)

        if last_name:
            emps = emps.filter(last_name__icontains = last_name)
        if dept:
            dept_id = Department.filter(dept_name=dept)
            emps = emps.filter(dept_id = dept)
        if role:
            emps = emps.filter(role_id = role)

        context ={
            "emps": emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An exception Occurred')




