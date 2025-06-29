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