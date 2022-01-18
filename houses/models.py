from django.db import models
from django.utils import timezone


class House(models.Model):
    """Model that defines the House table"""

    address = models.CharField(max_length=255)
    code = models.CharField(max_length=30)

    iptu_code = models.CharField(max_length=30)
    real_state_registry_code = models.CharField(max_length=30)
    area = models.IntegerField()

    tv_room = models.IntegerField()
    living_room = models.IntegerField()
    bedroom = models.IntegerField()
    office = models.IntegerField()
    cellar = models.IntegerField()
    bathroom = models.IntegerField()
    laundry_room = models.IntegerField()
    kitchen = models.IntegerField()
    more_details = models.CharField(max_length=255)
    parking_spaces = models.IntegerField()

    elevator = models.BooleanField()
    piped_gas = models.BooleanField()
    gas_included_in_the_condominium_price = models.BooleanField()
    water_included_in_the_condominium_price = models.BooleanField()

    rent_amount = models.IntegerField()
    condominium_price = models.IntegerField()
    situation = models.CharField(max_length=10)
    property_value = models.IntegerField()
    # property_plan = models.ImageField(use_url='../static/plans')

    responsible = models.CharField(max_length=50)

    updated_at = models.DateField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
