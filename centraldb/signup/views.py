from django.shortcuts import render
from .manage_user import *


def index_no_domain(request):
    return signin_no_domain(request)


def index(request, domain):
    try:
        print_warning(domain)
        dom = Domain.objects.get(name=domain)
    except Exception as e:
        print_error('Can\'t identify the domain' + str(e))
        return HttpResponseRedirect('/')
    request.session['id_dom'] = dom.id
    return login_domain_render(request)
