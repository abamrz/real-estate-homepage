from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


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

        # Inquiry made check
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Inquiry already made')
                return redirect('/listing/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          message=message, user_id=user_id, realtor_email=realtor_email)
        contact.save()

        # Send mail
        send_mail(
            'Property object inquiry',
            'Inquiry for ' + listing + 'has been made.',
            'email_address',
            [realtor_email, 'his_email'],
            fail_silently=False
        )

        messages.success(request, 'Your request is submitted')
        return redirect('/listing/' + listing_id)
