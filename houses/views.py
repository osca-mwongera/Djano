from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import House, Category
from django.db.models import Q


# Create your views here.


def house_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    houses = House.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        houses = houses.filter(category=category)
    query = request.GET.get('query')
    if query:
        houses = House.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    return render(request, 'houses/houses.html', {'category': category, 'categories': categories, 'houses': houses})


def house_detail(request, id, slug):
    house = get_object_or_404(House, id=id, slug=slug, available=True)
    return render(request, 'houses/detail.html', {'house': house})


def house_data(request, id, slug):
    house = serialize('geojson', House.objects.filter(id=id, slug=slug))
    return HttpResponse(house, content_type='json')
