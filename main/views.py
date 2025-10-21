from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Hardcoded sample users
        if username == 'hr@scube.com' and password == 'hr123!':
            return redirect('hr_dashboard')
        elif username == 'employeedemo@gmail.com' and password == 'emp123':
            return redirect('employee_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials!'})

    return render(request, 'login.html')

def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')

def employee_dashboard(request):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render(request, 'employee_dashboard.html', {'days': days})
