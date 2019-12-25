from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, state_choices, bedroom_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'listings': listings,
        'states': state_choices,
        'price': price_choices,
        'bedroom': bedroom_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvps = Realtor.objects.all().filter(is_mvp=True)
    context = {
        "realtors": realtors,
        "mvp_realtors": mvps
    }
    return render(request, 'pages/about.html', context)
