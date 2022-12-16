from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default="", blank=True)
    menuImage = models.ImageField(upload_to='img/menus', default='default.png',blank=True)

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Menu_detail", kwargs={"pk": self.pk})

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    itemImg = models.ImageField(upload_to='img/items/', default='default.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    menu = models.ForeignKey(Menu, default=None, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Item")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})
    
class DTable(models.Model):
    seats = models.IntegerField(default=0)
    location = models.CharField(max_length=50, default="", blank=True)
    

    class Meta:
        verbose_name = _("DTable")
        verbose_name_plural = _("DTables")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DTable_detail", kwargs={"pk": self.pk})
    
class Order(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    status = models.CharField(default="placed", max_length=10)
    table = models.ForeignKey(DTable,on_delete=models.CASCADE, default=None)
    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})


