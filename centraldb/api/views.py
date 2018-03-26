from django.shortcuts import render
from django.http import HttpResponseRedirect
from admin_centraldb.models import Domain, People, Modules, ModuleToDomain, DomPeople
from rent_place.models import Place, MetaDataPlace
from rent_place.models import MetaDataPlace
from centraldb.libs.printable import *
from django.http import HttpResponse
from django.db import transaction
from decimal import *

# Create your views here.


@transaction.atomic
def populate():
    remove_all()
    d = Domain(name='chateaudesvaux')
    d.save()
    add_module('a', d)
    add_module('b', d)
    add_module('module_rent_place', d)
    create_admin(d, 'w4pity@gmail.com')
    create_admin(d, 'w4pity1@gmail.com')
    create_admin(d, 'w4pity2@gmail.com')
    create_admin(d, 'w4pity@3gmail.com')
    for i in range(1, 10):
        add_place(d, 1, 'place ' + str(i), 'type' + str(i), 100 + i, 10 + i, 50 + i)
    print("Done populating")


def remove_all():
    Domain.objects.all().delete()
    DomPeople.objects.all().delete()
    People.objects.all().delete()
    Place.objects.all().delete()
    MetaDataPlace.objects.all().delete()


def create_admin(dom, mail):
    p = People(email=mail, mdp='base')
    p.set_password('aaaa')
    p.role = 0
    p.save()
    DomPeople(domain=dom, people=p).save()


def add_module(name, dom):
    m = Modules(table_name=name, display_name=name, link_name=name)
    m.save()
    ModuleToDomain(domain=dom, module=m).save()


def add_place(dom, state, name, type, price, tva, membre):
    cond = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, '
    p = Place(domain=dom, state=state, display_name=name, type_place=type, price=price, tva=tva, max_member=membre, condition=cond)
    p.save()
    MetaDataPlace(domain=dom, type_meta='primary_image', place=p).save()
    MetaDataPlace(domain=dom, type_meta='second_image', place=p).save()
    MetaDataPlace(domain=dom, type_meta='second_image', place=p).save()
    for i in range(1, 3):
        MetaDataPlace(domain=dom,
                      display_name='option' + str(i),
                      type_meta='option',
                      text='text for the option' + str(i),
                      option_tva=1,
                      option_number=2 + i,
                      option_price=1,
                      place=p).save()
