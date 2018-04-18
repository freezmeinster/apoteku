from django.db import models

class Obat(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
       return self.nama
