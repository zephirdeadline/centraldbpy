from django.shortcuts import render
from .forms import DelForm
from .manage_places import *
from centraldb.libs.security import check_signin
from admin_centraldb.views import get_list_modules


# Create your views here.


################################### ADMINISTRATION ###############################################


@check_signin
def admin_rent_place(request):
    add_place(request)
    modules_list = get_list_modules(request)
    place_metadata_list = get_metadata_places_domain(request)
    add_form = AddForm()
    update_form = UpdateForm()
    del_form = DelForm()
    return render(request, 'rent_place/admin_manage_place.html', {'modules_list': modules_list,
                                                                  'add_form': add_form,
                                                                  'update_form': update_form,
                                                                  'del_form': del_form,
                                                                  'places': place_metadata_list['places'],
                                                                  'meta': place_metadata_list['metadata_list'],
                                                                  'primary_image': place_metadata_list['primary_image']})


@check_signin
def admin_configure(request, id_place):
    update_place(request, id_place)
    add_image_to_place(request, id_place)
    # TODO not sure
    add_option_to_place(request)

    list_options = MetaDataPlace.objects.filter(
        domain_id=request.session['id_dom'],
        place_id=id_place,
        type_meta='option')
    meta_image_form = MetaDataImageForm()
    meta_option_form = MetaDataOptionForm()
    place = Place.objects.get(id=id_place)
    place_name = place.display_name
    update_form = UpdateForm(instance=place)
    modules_list = get_list_modules(request)
    return render(request, 'rent_place/admin_configure.html', {
        'id': id_place,
        'place_name': place_name,
        'modules_list': modules_list,
        'meta_image_form': meta_image_form,
        'meta_option_form': meta_option_form,
        'list_options': list_options,
        'update_form': update_form})


@check_signin
def admin_delete(request, id):
    delete_place(request, id)


#################################################" USER #####################################################

@check_signin
def user_rent_place(request):
    modules = get_list_modules(request)
    places = Place.objects.filter(id_dom_id=request.session['id_dom'])
    meta_primary_images = {}
    for place in places:
        meta_primary_images[place.id] = MetaDataPlace.objects.get(id_item=place, type_meta='primary_image')

    return render(request, 'rent_place/user_rent_place_home.html',
                  {'modules_list': modules, 'places': places, 'meta_primary_image': meta_primary_images})


@check_signin
def user_rent(request, id_place):
    modules = get_list_modules(request)
    place = Place.objects.get(id=id_place)
    meta_primary_image = MetaDataPlace.objects.get(idItem=place, type_meta='primary_image')
    meta_options = MetaDataPlace.objects.filter(idItem=place, type_meta="option")
    meta_second_images = MetaDataPlace.objects.filter(idItem=place, type_meta="second_image")
    return render(request, 'rent_place/user_rent.html', {
        'modules_list': modules,
        'place': place,
        'meta_primary_image': meta_primary_image,
        'meta_options': meta_options,
        'meta_second_images': meta_second_images
    })
