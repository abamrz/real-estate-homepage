from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          message=message, user_id=user_id, realtor_email=realtor_email)
        contact.save()
        messages.success(request, 'Your request is submitted')
        return redirect('/listing/' + listing_id)
