from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func



def allowed_user(allow_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allow_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorize')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('student')
        
        if group == 'faculty':
            return redirect('faculty')
        
        if group == 'registrar':
            return redirect('registrar')
        
        if group == 'guidance':
            return redirect('guidance')
        
        if group == 'admission':
            return redirect('admission')
        
        if group == 'accounting':
            return redirect('accounting')
        
        if group == 'schooladmin':
            return redirect('schooladmin')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
        if group == 'cashier':
            return redirect('cashier')


    return wrapper_func