from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100)
    origin_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'origin_date']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    designer = models.ForeignKey('auth.User', related_name='listings',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
