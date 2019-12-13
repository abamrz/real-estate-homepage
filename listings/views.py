from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
from listings.choices import price_choices, state_choices, bedroom_choices


# Create your views here.
def index(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query = query.filter(description__contains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['keywords']
        if city:
            query = query.filter(city__contains=city)

    # State
    if 'state' in request.GET:
        state = request.GET['keywords']
        if state:
            query = query.filter(state__contains=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['keywords']
        if bedrooms:
            query = query.filter(bedroom_choices=bedrooms)

    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedrooms_choices': bedroom_choices,
        'listing': query,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)