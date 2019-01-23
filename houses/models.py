from django.contrib.gis.db import models

from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'type'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('houses:house_list_by_type', args=[self.slug])


class County(models.Model):
    objectid = models.BigIntegerField()
    unit_area = models.FloatField()
    unit_perim = models.FloatField()
    district = models.CharField(max_length=50)
    count_field = models.FloatField()
    county_nam = models.CharField(max_length=50)
    code = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.county_nam

    class Meta:
        ordering = ('county_nam',)
        verbose_name = 'county'
        verbose_name_plural = 'counties'

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


class House(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Houses')
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, )
    available = models.BooleanField(default=True)
    time_added = models.DateTimeField(auto_now_add=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    geometry = models.PolygonField(srid=4326)
    description = models.TextField()
    photo = models.ImageField(upload_to='houses/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time_added',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('houses:house_detail', args=[self.id, self.slug])
