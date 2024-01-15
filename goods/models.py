from unicodedata import category
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self):
        return self.name
    
        
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Imagen')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Precio')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Descuento en %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Categoría")
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering=("id", )
        
    def __str__(self):
        return f'{self.name}. Cantidad {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        
        return self.price