from django.db import models

class Pelanggan(models.Model):
    nama = models.CharField(max_length=255)
    
    def __str__(self):
       return self.nama

class Resep(models.Model):
    pelanggan = models.ForeignKey("transaksi.Pelanggan", on_delete=models.CASCADE)
    
    def __str__(self):
       return self.pelanggan.nama

class BarisResep(models.Model):
    resep = models.ForeignKey("transaksi.Resep", on_delete=models.CASCADE)
    obat = models.ForeignKey("gudang.Obat", on_delete=models.CASCADE)
    jumlah = models.IntegerField()

    def __str__(self):
       return self.obat.nama
