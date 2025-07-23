from django.db import models

class FeaturedItem(models.Model):
    name = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured/')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('item_detail', args=[self.slug])

    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='farms/')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    """Individual produce items available for purchase."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.name