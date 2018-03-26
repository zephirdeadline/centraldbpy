from .forms import *
from admin_centraldb.models import DomPeople, Domain
from django.http import HttpResponseRedirect
from hashlib import sha1
from centraldb.libs.printable import *
from django.db import transaction
from django.shortcuts import render
from admin_centraldb.forms import NewAccountForm


def is_present(form, id_dom):
    p = People.objects.filter(email=form.cleaned_data['email'])
    return p.exists() and DomPeople.objects.filter(domain_id=id_dom).exists()


def get_user(form):
    p = People.objects.get(email=form.cleaned_data['email'], mdp=sha1(str(form.cleaned_data['mdp']).encode()).hexdigest())
    return p


@transaction.atomic
def add_people_from_form(request):
    form = NewAccountForm(request.POST)
    if form.is_valid() and not is_present(form, request.session['id_dom']):
        try:
            people = form.save(commit=False)
            people.mdp = sha1(str(people.mdp).encode()).hexdigest()
            people.save()
            DomPeople(domain_id=request.session['id_dom'], people=people).save()
            print_success("Success to save people")
            return True
        except Exception as e:
            print_error("fail to save people: " + str(e))
    else:
        print_error("The form to save people fail")


def gen_password(password):
    return sha1(str(password).encode()).hexdigest()


@transaction.atomic
def save_people(request, dom):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid() and not is_present(form, request.session['id_dom']):
            try:
                people = form.save(commit=False)
                people.mdp = gen_password(people.mdp)
                people.save()
                DomPeople(domain_id=request.session['id_dom'], people=people).save()
                print_success("Success to register")
                set_session(request, people, request.session['id_dom'])
                return HttpResponseRedirect('/user/')
            except Exception as e:
                print_warning("Fail to save " + str(e))
        else:
            print_warning("Fail to Register")
            redirect_to_main()
    else:
        print_warning("Default signup")
        form_signin = SigninForm()
        form_signup = SignupForm()
        print_success(dom.login_image.name)
        return render(request, 'signup/index.html',
                      {'form_signin': form_signin,
                       'form_signup': form_signup,
                       'dom': dom})


def set_session(request, people, id_dom, role):
    request.session['email'] = people.email
    request.session['id'] = people.id
    request.session['id_dom'] = id_dom
    request.session['role'] = role


def redirect_to_main():
    return HttpResponseRedirect("/")


def connect_people_with_domain(request):
    id_dom = request.session['id_dom']
    form = SigninForm(request.POST)
    if form.is_valid():
        try:
            people = get_user(form)
            return connect_people(request, id_dom, people)
        except Exception as e:
            print_error('bad login' + str(e))
            return redirect_to_main()
    return redirect_to_main()


def connect_people(request, id_dom, people):
        role = people.role
        state = people.state
        if (role == 0) or (role == 1 and state != 3):
            set_session(request, people, id_dom, role)
            print_success("Success to Login as admin")
            return HttpResponseRedirect('/admin/')
        elif role == 2 and state != 3:
            set_session(request, people, id_dom, role)
            print_success("Success to Login as user")
            return HttpResponseRedirect('/user/')
        else:
            print_warning("Account blocked")
            return redirect_to_main()


def connect_people_without_domain(request):
    form = SigninForm(request.POST)
    if form.is_valid():
        try:
            people = get_user(form)
            id_dom = DomPeople.objects.get(people_id=people.id).domain_id
            return connect_people(request, id_dom, people)
        except Exception as e:
            print_error('bad login' + str(e))
            return redirect_to_main()
    return redirect_to_main()


def signup(request):
    if request.method == 'POST':
        return save_people(request)
    else:
        return login_domain_render(request)


def signin(request):
    if request.method == 'POST':
        return connect_people_with_domain(request)
    else:
        return login_domain_render(request)


def login_domain_render(request):
    dom_id = request.session['id_dom']
    dom = Domain.objects.get(id=dom_id)
    print_warning("View sign")
    form_signin = SigninForm()
    form_signup = SignupForm()
    return render(request, 'signup/index.html',
                  {'form_signin': form_signin,
                   'form_signup': form_signup,
                   'dom': dom})


def signin_no_domain(request):
    if request.method == 'POST':
        return connect_people_without_domain(request)
    else:
        form_signin = SigninForm()
        print_success('Access login with no domain')
        return render(request, 'signup/index_no_domain.html',
                      {'form_signin': form_signin})


def logout(request):
    try:
        name_dom = Domain.objects.get(id=request.session['id_dom']).name
        url = '/login/domain/' + name_dom
    except:
        url = '/'
    request.session.flush()
    return HttpResponseRedirect(url)

