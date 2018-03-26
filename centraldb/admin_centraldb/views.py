from django.shortcuts import render
from .models import Domain, People, DomPeople, Modules, ModuleToDomain
from .forms import *
from centraldb.libs.security import *
from centraldb.libs.printable import *
from django.http import HttpResponseRedirect
from signup.views import is_present
from django.core.mail import send_mail
from django.db import transaction
from centraldb.libs.request_helper import get_list_modules
from signup.manage_user import add_people_from_form
# Create your views here.


@check_signin
@check_admin
def index_admin(request):
    modules_list = get_list_modules(request)
    return render(request, 'admin_centraldb/main_admin.html', {'modules_list': modules_list})


@check_signin
@check_admin
def domain_setting(request):
    if request.method == 'POST':
        instance = Domain.objects.get(id=request.session['idDom'])
        form = SettingDomainForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():#and not Domain.objects.filter(name = instance.name).exists():#TODO change if name unchange
            form.save()
            print_success("Config Domain setting saved success")
            return HttpResponseRedirect("/admin/")
        else:
            print_error("fail to save change " + repr(form.errors))
    else:
        dom = Domain.objects.get(id=request.session['idDom'])#TODO
        form = SettingDomainForm(instance=dom)
    modules_list = get_list_modules(request)
    return render(request, 'admin_centraldb/domain_setting.html', {'form': form, 'modulesList': modules_list})


@check_signin
@check_admin
def account_setting(request):
    if request.method == 'POST':
        instance = People.objects.get(id=request.session['id'])
        form = SettingAccountForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin/")
    else:
        account = People.objects.get(id=request.session['id'])#TODO
        form = SettingAccountForm(instance=account)

    modules_list = get_list_modules(request)
    return render(request, 'admin_centraldb/account_setting.html', {'form': form, 'modules_list': modules_list})


@check_signin
@check_admin
@transaction.atomic
def add_new_people(request):
    if request.method == 'POST':
        add_people_from_form(request)
    form = NewAccountForm()
    modules_list = get_list_modules(request)
    return render(request, 'admin_centraldb/add_new_people.html', {'form': form, 'modules_list': modules_list})


@check_signin
@check_admin
def list_people(request):
    peoples = People.objects.order_by('state', 'role')
    modules_list = get_list_modules(request)
    return render(request, "admin_centraldb/list_people.html", {'peoples': peoples, 'modules_list' : modules_list})


@check_signin
@check_admin
@transaction.atomic
def delete(request, id):
    try:
        People.objects.get(id=id).delete()
        DomPeople.objects.get(idPeople = id).delete()
    except Exception as e:
        print_error("Fail to delete poeple -> " + str(e))
    return HttpResponseRedirect('/admin/list_people/')


@check_signin
@check_admin
def deblock(request, id):
    p = People.objects.get(id=id)
    p.state = 1
    p.save()

    return HttpResponseRedirect('/admin/list_people/')


@check_signin
@check_admin
def block(request, id):
    p = People.objects.get(id=id)
    p.state = 2
    p.save()

    return HttpResponseRedirect('/admin/list_people/')


@check_signin
@check_admin
def contact(request, id):
    member_to = People.objects.get(id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                mail = form.save(commit=False)
                mail.domain_id = request.session['id_dom']
                mail.To = member_to
                mail.From = request.session['id']
                mail.save()
                send_mail(
                    mail.subject,
                    mail.content,
                    request.session['email'],
                    [member_to.email],
                    fail_silently=False,
                )
                print_success("Success to register")
                return HttpResponseRedirect('/admin/')
            except:
                print_warning("Fail to save mail")
        else:
            print_warning("Fail to valid form mail")
    else:
        form = ContactForm()
    modules_list = get_list_modules(request)
    return render(request, 'admin_centraldb/contact.html', {
        'form': form,
        'modules_list' : modules_list,
        'member_to': member_to})


def ask_module(request):
    return render(request, 'admin_centraldb/ask_module.html')