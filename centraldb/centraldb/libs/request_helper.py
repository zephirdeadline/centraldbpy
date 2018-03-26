from admin_centraldb.models import Modules

def get_list_modules(request):
    modules = Modules.objects.filter(moduletodomain__domain_id=request.session['id_dom'])
    return modules