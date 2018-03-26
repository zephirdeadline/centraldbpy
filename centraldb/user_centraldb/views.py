from centraldb.libs.security import *
from django.shortcuts import render
from centraldb.libs.request_helper import get_list_modules
# Create your views here.

@check_signin
def user(request):
    modules_list = get_list_modules(request)
    return render(request, 'user_centraldb/user.html', {'modules_list': modules_list})
