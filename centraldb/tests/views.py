
from django.shortcuts import render
from admin_centraldb.models import People, Domain, DomPeople, Modules, ModuleToDomain
from django.http import HttpResponseRedirect
from datetime import datetime
from centraldb.libs.printable import *

def test(request):
    dom = ModuleToDomain(idDom_id=2, idMod_id=2)
    try:
        dom.save()
        print_success('test saved OK')
    except:
        print_error('test not saved')
    return HttpResponseRedirect('/')
