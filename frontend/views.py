from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    return render(request, 'frontend/index.html')
    
def service(request):
    return render(request, 'frontend/services.html',{"nbar":"service"})
    
def blog(request):
    return render(request, 'frontend/blog.html',{"nbar":"blog"})
    
def contact(request):
    if request.method == "POST":
        if not request.POST.get("message"):
            messages.error(request, 'Please enter message')
            return redirect('frontend:contact')
        if not request.POST.get("subject"):
            messages.error(request, 'Please enter subject')
        if not request.POST.get("name"):
            messages.error(request, 'Please enter name')
        if not request.POST.get("email"):
            messages.error(request, 'Please enter email')
            return redirect('frontend:contact')
        if not request.POST.get("phone"):
            messages.error(request, 'Please enter phone number')
            return redirect('frontend:contact')
        
        if not request.POST.get("loan"):
            messages.error(request, 'Please enter required loan amount')
            return redirect('frontend:contact')
        
        if not request.POST.get("gender"):
            messages.error(request, 'Please enter gender')
            return redirect('frontend:contact')
        if not request.POST.get("state"):
            messages.error(request, 'Please enter state')
            return redirect('frontend:contact')
        if not request.POST.get("city"):
            messages.error(request, 'Please enter city')
            return redirect('frontend:contact')
        


        subject = request.POST.get("subject")
        details =  f'NAME : {request.POST.get("name")} , EMAIL : {request.POST.get("email")}, PHONE NUMBER : {request.POST.get("phone")} , ARE YOU ON WHATSAPP WITH SAME NUMBER : {request.POST.get("type")} , REQUIRED LOAD AMOUNT : {request.POST.get("loan")} , GNEDER : {request.POST.get("gender")} , STATE : {request.POST.get("state")} , CITY : {request.POST.get("city")} , MESSAGE : {request.POST.get("message")}  '

        from_email = request.POST.get("email")
        recipient_list = ['info.giandhan@gmail.com']
        print(subject,details,from_email,recipient_list)
        email = send_mail(subject, details, from_email, recipient_list)
        print(email,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
        if email == 1:
            messages.error(request, 'success')
        else:
            messages.error(request, 'Error while sending the email')

        return redirect('frontend:contact')
    return render(request, 'frontend/contact.html',{"nbar":"contact"})
    
    
