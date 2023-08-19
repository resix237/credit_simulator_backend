from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Credit
        fields = ("id", "montant_emprunte", "taux_interet", "duree_credit", "date_fincredit")