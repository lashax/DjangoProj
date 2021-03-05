from django.db import models


class Clothes(models.Model):
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
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'
