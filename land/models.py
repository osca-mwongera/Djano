from django.contrib.gis.db import models

from django.urls import reverse

from django.utils import timezone


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('land:parcel_list_by_category', args=[self.slug])


class County(models.Model):
    objectid = models.BigIntegerField()
    unit_area = models.FloatField()
    unit_perim = models.FloatField()
    district = models.CharField(max_length=50)
    count_field = models.FloatField()
    county_nam = models.CharField(max_length=50, db_index=True)
    code = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        ordering = ('county_nam',)
        verbose_name = 'county'
        verbose_name_plural = "counties"

    def __str__(self):
        return self.county_nam

    def get_absolute_url(self):
        return reverse('land:parcel_list_by_county', args=[self.county_nam])


class District(models.Model):
    distname = models.CharField(max_length=20, db_index=True)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        ordering = ('distname',)
        verbose_name = 'district'
        verbose_name_plural = "districts"

    def __str__(self):
        return self.distname


class Parcel(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    owner = models.CharField(max_length=300, db_index=True)
    title_number = models.CharField(max_length=70)
    area = models.FloatField(max_length=5)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    geometry = models.PolygonField(srid=4326, geography=True)
    photo = models.ImageField(upload_to='parcels/%Y/%m/%d')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Parcels')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-added',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('land:parcel_detail', args=[self.id, self.slug])

