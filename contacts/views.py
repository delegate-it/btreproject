from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method=='POST':

        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if the property is already enquiried by the customer
        if user_id:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)

        if has_contacted:
            messages.warning(request, 'You already have contacted the realtor for this property')
            return redirect('/listings/' + listing_id)


        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        send_mail('Property listing enquiry', 'There has been an enquiry for ' + listing + '. Sign into the admin panel for more information','nicelhage@gmail.com', [realtor_email, 'nicelhage@hotmail.com'],fail_silently=False )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + listing_id)