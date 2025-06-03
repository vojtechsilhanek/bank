from django.db import models



def vek(value):
    if value < 18:
        raise TypeError("Nezletilý")


class Customers(models.Model):
    jmeno = models.CharField(max_length=20)
    prijmeni = models.CharField(max_length=20)
    vek = models.IntegerField(validators=[vek])
    adresa = models.CharField(max_length=50)

    POHLAVI_CHOICES = [
        ("M", "Muž"),
        ("Z", "Žena"),
        ("N", "Nechci zmiňovat")
    ]
    pohlavi = models.CharField(max_length=1, choices=POHLAVI_CHOICES)

    telefon = models.CharField(max_length=9)

    def __str__(self):
        return self.prijmeni


class Account(models.Model):
    zakaznik = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="accounts")
    cislo = models.IntegerField()

    TYP_UCTU_CHOICES = [
        ("B", "Běžný účet"),
        ("S", "Spořící účet"),
        ("U", "Úvěrový účet")
    ]
    typ_uctu = models.CharField(max_length=1, choices=TYP_UCTU_CHOICES)

    MENA_CHOICES = [
        ("CZK", "ČESKÁ KORUNA"),
        ("EUR", "EURO"),
        ("USD", "DOLLAR")
    ]
    mena = models.CharField(max_length=3, choices=MENA_CHOICES)

    def __str__(self):
        return f"{self.get_typ_uctu_display()} ({self.cislo})"

# 
class Transactions(models.Model):
    TRANSAKCE_TYP_CHOICES = [
        ("V", "Vklad"),
        ("VY", "Výběr"),
        ("P", "Platba")
    ]
    zakaznik = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="transactions")
    typ_transakce = models.CharField(max_length=2, choices=TRANSAKCE_TYP_CHOICES)
    castka = models.DecimalField(max_digits=10, decimal_places=2)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_typ_transakce_display()} - {self.castka} CZK"
