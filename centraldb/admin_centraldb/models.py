from django.db import models
from hashlib import sha1

# Create your models here.
from django.db import models


# Create your models here.

class DomPeople(models.Model):
    domain = models.ForeignKey('admin_centraldb.Domain', on_delete=models.CASCADE)
    people = models.ForeignKey('People', on_delete=models.CASCADE)

    def __str__(self):
        return str(id)


class Domain(models.Model):
    name = models.CharField(max_length=64, unique=True)
    web_site = models.CharField(max_length=64, default='Unknown', unique=True)
    date_save = models.DateTimeField(auto_now_add=True)
    login_image = models.FileField(upload_to='static/uploads/', default='static/uploads/centraldb.jpeg')
    slug = models.CharField(max_length=64, default='Unknown')
    name_factorisation = models.CharField(max_length=64, default='Unknown')
    logo_factorisation = models.FileField(upload_to='static/uploads/', default='static/uploads/centraldb.jpeg')
    address_factorisation = models.CharField(max_length=64, default='Unknown')
    phone = models.CharField(max_length=64, default='Unknown')
    siret = models.CharField(max_length=64, default='Unknown')
    ape = models.CharField(max_length=64, default='Unknown')
    rcs = models.CharField(max_length=64, default='Unknown')
    pref_invoice = models.CharField(max_length=64, default='Unknown')
    tva_number = models.CharField(max_length=64, default='Unknown')

    def __str__(self):
        return "hello"


class ModuleToDomain(models.Model):
    domain = models.ForeignKey('admin_centraldb.Domain', on_delete=models.CASCADE)
    module = models.ForeignKey('Modules', on_delete=models.CASCADE)

    def __str__(self):
        return str(id)


class Modules(models.Model):
    table_name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)
    link_name = models.CharField(max_length=64)

    def __str__(self):
        return str(id)


class People(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    # 0 superuser 1 admin 2 user

    role_select = (
        (1, 'Administrateur'),
        (2, 'Utilisateur'),
    )
    role = models.IntegerField(default=2, choices=role_select)
    # 1 accepted 2 waiting 3 blocked
    state = models.IntegerField(default=2)
    mdp = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    date_last_con = models.DateTimeField(auto_now=True)
    date_sign = models.DateTimeField(auto_now_add=True)
    addr = models.CharField(max_length=64, default="unknow")
    code_postal = models.CharField(max_length=64, default="unknow")
    city = models.CharField(max_length=64, default="unknow")
    is_first_connection = models.BooleanField(default=True)

    def set_password(self, string):
        self.mdp = sha1(string.encode()).hexdigest()

    def __str__(self):
        return str(id)


class Contact(models.Model):
    domain = models.ForeignKey('admin_centraldb.Domain', on_delete=models.CASCADE)
    subject = models.CharField(max_length=64)
    content = models.TextField()
    people = models.ForeignKey('People', related_name='To', on_delete=models.CASCADE)
    domain = models.ForeignKey('admin_centraldb.Domain', related_name='From', on_delete=models.CASCADE)
