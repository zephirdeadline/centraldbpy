from centraldb.libs.printable import *
from rent_place.forms import AddForm, UpdateForm, MetaDataImageForm, MetaDataOptionForm
from admin_centraldb.models import Domain
from django.http import HttpResponseRedirect
from .models import Place, MetaDataPlace


def add_place(request):
    if request.method == 'POST':
        add_form = AddForm(request.POST)
        if add_form.is_valid():
            try:
                place = add_form.save(commit=False)
                place.id_dom = Domain.objects.get(id=request.session['id_dom'])
                place.save()
                place_id = place.pk
                print_success("Success to Add the place")
                return HttpResponseRedirect('/module_rent_place/configure/' + str(place_id) + '/#update')
            except Exception as e:
                print_warning("Fail to save form add a place -> " + str(add_form.errors) + str(e))
        else:
            print_warning("Fail to valid form add a place " + str(add_form.errors))


def get_metadata_places_domain(request):
    meta = {}
    primary_image = {}
    places = Place.objects.filter(domain_id=request.session["id_dom"])
    for r in places:
        try:
            meta[r.pk] = MetaDataPlace.objects.filter(
                type_meta="option",
                domain_id=request.session["id_dom"],
                place_id=r.pk)
            primary_image[r.pk] = MetaDataPlace.objects.filter(
                type_meta="primary_image",
                domain_id=request.session["id_dom"],
                place_id=r.pk)
        except Exception as e:
            print_warning("Fail to get meta -> " + str(e))
    return {'places': places, 'metadata_list': meta, 'primary_image': primary_image}


def update_place(request, id_place):
    if 'info_form' in request.POST and request.method == 'POST':
        try:
            instance = Place.objects.get(id=id_place)
            place = UpdateForm(request.POST, instance=instance)
            place.save()
            print_success("Success to Update the place")
            return HttpResponseRedirect('/module_rent_place/admin')
        except Exception as e:
            print_warning("Fail to update the place -> " + str(e))
    else:
        print_warning("Fail to valid form update place")


def add_image_to_place(request, id_place):
    if 'add_image_form' in request.POST and request.method == 'POST':
        meta_image_form = MetaDataImageForm(request.POST, request.FILES)
        try:
            if meta_image_form.is_valid():
                meta_image_form = meta_image_form.save(commit=False)
                meta_image_form.id_dom = Domain.objects.get(id=request.session['id_dom'])
                meta_image_form.type_meta = 'primary_image'
                meta_image_form.id_item_id = id_place
                meta_image_form.save()
                HttpResponseRedirect('/module_rent_place/admin/configure/' + str(id_place) + '/')
            else:
                print_error("fail to save -> " + str(meta_image_form.errors))
        except Exception as e:
            print_warning("Fail to save form add a place -> " + str(meta_image_form.errors) + str(e))


def add_option_to_place(request):
    if 'add_option_form' in request.POST and request.method == 'POST':
        meta_option_form = MetaDataOptionForm(request.POST)
        try:
            if meta_option_form.is_valid():
                meta_option_form = meta_option_form.save(commit=False)
                meta_option_form.id_dom = Domain.objects.get(id=request.session['idDom'])
                meta_option_form.type_meta = 'option'
                meta_option_form.idItem_id = id
                meta_option_form.save()
                HttpResponseRedirect('/module_rent_place/admin/configure/' + str(id) + '/#add')
            else:
                print_error("fail to save -> " + str(meta_option_form.errors))
        except Exception as e:
            print_warning("Fail to save form add a place -> " + str(meta_option_form.errors) + str(e))


def update(request):
    if 'update_form' in request.POST and request.method == 'POST':
        pass


def delete_place(request, id_place):
    try:
        Place.objects.get(id=id_place, id_dom=request.session['id_dom']).delete()
        print_success("Success to delete the place")
        # MetaDataPlace.objects.filter(id_item=id).delete()
        # print_success("Success to delete place's Meta")
        return HttpResponseRedirect('/module_rent_place/')
    except Exception as e:
        print_warning("Fail to delete the place: " + str(e))
    return HttpResponseRedirect("/module_rent_place/")
