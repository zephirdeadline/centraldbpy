from django.db import models


# Create your models here.

class MetaDataPlace(models.Model):
    domain = models.ForeignKey('admin_centraldb.Domain', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=64, default="")
    choose_type_meta = (
        ('option', 'Option'),
        ('primary_image', 'Image Principale'),
        ('second_image', 'Images secondaires'),
    )
    type_meta = models.CharField(max_length=64, default='')
    text = models.TextField(max_length=255, default='')
    place = models.ForeignKey('Place')
    path_image = models.FileField(upload_to='static/uploads/', default="static/uploads/default-img.gif")
    option_tva = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    option_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    option_number = models.CharField(max_length=255, default=0.0)


class Place(models.Model):
    domain = models.ForeignKey('admin_centraldb.Domain', on_delete=models.CASCADE)
    # 1 libre, 2 reserver, 3 occupé
    state = models.IntegerField(default=1)
    display_name = models.CharField(max_length=64)
    type_place = models.CharField(max_length=64, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tva = models.DecimalField(max_digits=6, decimal_places=2)
    max_member = models.IntegerField(default=0)
    condition = models.TextField(default="")

    def __str__(self):
        return str(id)


class RentedPlace(models.Model):
    state = models.CharField(max_length=64)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    people = models.ForeignKey('admin_centraldb.People', on_delete=models.CASCADE)
    penalties = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.TextField(max_length=255)
    place = models.ForeignKey('Place')
    domain = models.ForeignKey('admin_centraldb.Domain', on_delete=models.CASCADE)
    date_rented = models.DateTimeField(auto_now_add=True, auto_now=False)
    # estimate_number
    # link
    state_invoice = models.IntegerField()

    def __str__(self):
        return str(id)


class RentedPlaceOption(models.Model):
    rented_place = models.ForeignKey('RentedPlace', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    label2 = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tva = models.DecimalField(max_digits=6, decimal_places=2)
    number = models.IntegerField()

    def __str__(self):
        return str(id)


class TypePlace(models.Model):
    domain = models.ForeignKey('admin_centraldb.Domain', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=64)
    link_name = models.CharField(max_length=64)

    def __str__(self):
        return str(id)
