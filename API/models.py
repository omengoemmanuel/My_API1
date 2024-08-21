from django.db import models


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    photo = models.ImageField(upload_to='products', default='product/product.jpg')

    def __str__(self):
        return self.name
