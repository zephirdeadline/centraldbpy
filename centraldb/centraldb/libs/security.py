from django.http import HttpResponseRedirect


def is_connected(request):
    return 'id' in request.session


def is_admin(request):
    return request.session['role'] == 1 or request.session['role'] == 0


def check_signin(func):
    def check(*args, **kwargs):
        if not is_connected(args[0]):
            return HttpResponseRedirect('/')
        return func(*args, **kwargs)
    return check


def check_admin(func):
    def check(*args, **kwargs):
        if is_admin(args[0]):
            return func(*args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return check