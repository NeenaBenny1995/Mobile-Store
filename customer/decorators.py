from django.shortcuts import redirect


def signin_required(function):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return function(request,*args,**kwargs)

    return wrapper


def admin_permission_required(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("")
        else:
            return func(request,*args,**kwargs)

    return wrapper
