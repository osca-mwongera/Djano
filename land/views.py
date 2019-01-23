from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Parcel, Category
from django.db.models import Q


# Create your views here.


def parcel_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    parcels = Parcel.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        parcels = parcels.filter(category=category)
    query = request.GET.get('query')
    if query:
        parcels = Parcel.objects.filter(
            Q(name__icontains=query) |
            Q(title_number__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
        if parcels.count() > 0:
            return render(request, 'land/land.html',
                          {'category': category, 'categories': categories, 'parcels': parcels})
        else:
            print('The parcel you searched for does not exist in our databases. I will look into this searches need to'
                  ' have some inspiration. They never return zero matches')
    return render(request, 'land/land.html', {'category': category, 'categories': categories, 'parcels': parcels})


def parcel_detail(request, id, slug):
    parcel = get_object_or_404(Parcel, id=id, slug=slug, available=True)
    return render(request, 'land/parcel.html', {'parcel': parcel})


def parcel_data(request, id, slug):
    parcels = serialize(
        'geojson',
        Parcel.objects.filter(id=id, slug=slug),
        geometry_field='geometry',
        fields='geometry')
    return HttpResponse(parcels, content_type='json')


#serialize('geojson', Parcel.objects.filter(id=id),
          #geometry_field='geom',
          #fields=('name', 'description',))

