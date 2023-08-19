from django.db import models
from django.utils import timezone
# Create your models here.
class Credit(models.Model):
    montant_emprunte = models.IntegerField (blank=False)
    taux_interet= models.IntegerField(blank=False)
    duree_credit = models.IntegerField(blank=False)
    date_fincredit = models.DateField()
    date_create = models.DateField(auto_now_add=True)
    ower = models.ForeignKey(
        "auth_users.UserGestion", on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_create']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.date_create = timezone.now()
        return super(Credit, self).save(*args, **kwargs)
    def __str__(self):
        return "Credit du {}".format(self.date_create)