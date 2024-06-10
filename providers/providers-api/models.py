from django.db import models


class Clinician(models.Model):
    # pac_id: Unique individual clinician ID assigned by PECOS
    pac_id = models.TextField(max_length=10)
    last_name = models.TextField(max_length=35)
    first_name = models.TextField(max_length=25)
    middle_name = models.TextField(max_length=25)
    gender = models.TextField(max_length=100)
    credential = models.TextField(max_length=100)
    # pri_specialty: primary specialty of clinician
    pri_specialty = models.TextField(max_length=100)
    facility_name = models.TextField(max_length=70)
    telehealth = models.TextField(max_length=100)
    # org_pac_id: Unique group ID assigned by PECOS to the group that
    # the individual clinician works with – will be blank if the
    # address is not linked to a group
    org_pac_id = models.TextField(max_length=10)
    # address line one
    address_ln_one = models.TextField(max_length=55)
    # address line two
    address_ln_two = models.TextField(max_length=55)
    # ln_two_supress: Marker that the address as reported may be incomplete
    ln_two_supress = models.TextField(max_length=1)
    city_town = models.TextField(max_length=30)
    state = models.TextField(max_length=2)
    zip_code = models.TextField(max_length=15)
    phone = models.TextField(max_length=20)
    ind_assign = models.TextField(max_length=1)
    grp_assign = models.TextField(max_length=1)

