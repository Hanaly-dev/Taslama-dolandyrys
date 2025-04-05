from django.db import models

from django.db import models

class Ulanyjy(models.Model):
    ady = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    adres = models.TextField()

    def __str__(self):
        return self.ady
    class Meta:
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'
class Enjam(models.Model):
    ady = models.CharField(max_length=255)
    mukdary = models.PositiveIntegerField()
    bahasy = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    suraty = models.ImageField(upload_to='media/',null=True, blank=True)

    def umumy_baha(self):
        return self.mukdary * self.bahasy

    def __str__(self):
        return self.ady
    class Meta:
        verbose_name = 'Enjam'
        verbose_name_plural = 'Enjamlar'



class Taslama(models.Model):
    GORNUS_CHOICES = [
        ('uly', 'Uly Taslama'),
        ('orta', 'Orta Taslama'),
        ('kici', 'Kiçi Taslama'),
    ]
    STATUS_CHOICES = [
        ('planlanan', 'Meýilleşdirilen'),
        ('dowam', 'Dowam edýär'),
        ('tamam', 'Tamamlandy')
    ]
    ady = models.CharField(max_length=255)
    müşderi = models.ForeignKey(Ulanyjy, on_delete=models.CASCADE,null=True, blank=True)
    gornusi = models.CharField(max_length=10, choices=GORNUS_CHOICES)
    baslanan_senesi = models.DateField()
    tamamlanjak_senesi = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    beyan = models.TextField(blank=True, null=True)
    enjamlary = models.ManyToManyField(Enjam, through='ProyektEnjam', related_name='proyektler')
    suraty=models.ForeignKey('Surat', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ady
    class Meta:
        verbose_name = 'Taslama'
        verbose_name_plural = 'Taslamalar'
class ProyektEnjam(models.Model):
    proyekt = models.ForeignKey(Taslama, on_delete=models.CASCADE)
    enjam = models.ForeignKey(Enjam, on_delete=models.CASCADE)
    mukdary = models.PositiveIntegerField(default=1)

    def umumy_baha(self):
        return f"{self.mukdary * self.enjam.bahasy} TMT"

    def __str__(self):
        return f"{self.proyekt.ady} – {self.enjam.ady} ({self.mukdary} sany)"
    class Meta:
        verbose_name = 'Proyekt Enjam'
        verbose_name_plural = 'Proyekt Enjamlary'

class Is_Hasabatlar(models.Model):
    proyekt = models.ForeignKey(Taslama, on_delete=models.CASCADE, related_name='isler')
    ady = models.CharField(max_length=255)
    tamamlandy = models.BooleanField(default=False)
    bellik = models.TextField(blank=True, null=True)
    baslanys_wagty = models.DateTimeField(blank=True, null=True)
    gutarany_wagty = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.proyekt.ady} – {self.ady}"
    class Meta:
        verbose_name = 'Is Hasabat'
        verbose_name_plural = 'Is Hasabatlar'

class Surat(models.Model):
    ady=models.CharField(max_length=255,null=True, blank=True)
    surat = models.ImageField(upload_to='media/')
    bellik = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.ady

    class Meta:
        verbose_name = 'Surat'
        verbose_name_plural = 'Suratlar'