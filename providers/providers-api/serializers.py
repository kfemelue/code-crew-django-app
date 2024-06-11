from rest_framework import serializers
from .models import Clinician


class ClinicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinician
        fields = [
            "pac_id",
            "last_name",
            "first_name",
            "middle_name",
            "gender",
            "credential",
            "pri_specialty",
            "facility_name",
            "telehealth",
            "org_pac_id",
            "address_ln_one",
            "address_ln_two",
            "ln_two_supress",
            "city_town",
            "state",
            "zip_code",
            "phone",
            "ind_assign",
            "grp_assign"
        ]
