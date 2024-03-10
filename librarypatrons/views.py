from django.shortcuts import render
from .models import *
from .forms import BookApplicantsForm
# Create your views here.
def searchbooks(request):
    return render(request,'librarianpatrols/searchbooks.html')

from librarian.models import BookDetails
def book_details_list(request):
    book_details_list = BookDetails.objects.all()
    return render(request, 'librarianpatrols/searchbooks.html',{'book_details_list':book_details_list})


def addlibpatronsprofile(request):
    return render(request,'librarianpatrols/addlibpatronsprofile.html')

def submit_form(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone_number=request.POST['phone_number']
        Branch=request.POST.get('Branch','')
        Year=request.POST.get('Year','')

        applicant=Applicant(first_name=first_name,last_name=last_name,phone_number=phone_number,Branch=Branch,Year=Year)

        applicant.save()
        return render(request, 'librarianpatrols/addlibpatronsprofile.html',{'applicants_list':applicants_list})
    return render(request, 'librarypatronshomepage.html',{'applicants_list':applicants_list})

# from django.shortcuts import render, redirect
# from .models import Applicant  # Import your Applicant model

# def submit_form(request):
#     if request.method == 'POST':
#         # Handle form submission
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         phone_number = request.POST['phone_number']
#         branch = request.POST.get('Branch', '')
#         year = request.POST.get('Year', '')
#
#         # Save the updated details to the user
#         user = request.user
#         user.first_name = first_name
#         user.last_name = last_name
#         user.phone_number = phone_number
#         user.branch = branch
#         user.year = year
#         user.save()
#
#         # Create or update the Applicant model
#         applicant, created = Applicant.objects.get_or_create(user=user)
#         applicant.first_name = first_name
#         applicant.last_name = last_name
#         applicant.phone_number = phone_number
#         applicant.Branch = branch
#         applicant.Year = year
#         applicant.save()
#
#         # Get the updated user details
#         updated_user = request.user
#
#         # Redirect to a success page or render a template with updated details
#         return render(request, 'librarypatronshomepage.html', {'user': updated_user, 'updated': True})
#
#     return render(request, 'librarypatronshomepage.html', {'updated': False})

def applicants_list(request):
    applicants_list = Applicant.objects.all()
    return render(request, 'librarianpatrols/addlibpatronsprofile.html',{'applicants_list':applicants_list})

from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import *
def get_the_book(request,book_id):
    book_details=get_object_or_404(BookDetails, id=book_id)
    if request.method=='POST':
        form = BookApplicantsForm(request.POST,request.FILES)
        if form.is_valid():
            book_application=form.save(commit=False)
            book_application.book_details=book_details
            book_application.save()

            subject='ID Card Received'
            message='Thank you for getting the book. Your details are received and will be sent to next process'
            from_email='anushamajji806@gmail.com'
            recipient_list=[book_application.email]
            send_mail(subject,message,from_email,recipient_list)
            return redirect('librarypatrons:book_details_list')
    else:
        form=BookApplicantsForm()

    return render(request,'librarianpatrols/get_this_book.html',{'book_details':book_details,'form':form})


from django.shortcuts import render, HttpResponse
from .models import contactus

def feedback(request):
    # You can keep the 'feedback' view as is or update it according to your requirements
    return render(request, 'librarianpatrols/feedback.html')


from django.core.mail import send_mail
from django.shortcuts import HttpResponse
from .models import contactus


def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        book_id = request.POST['book_id']
        feedback = request.POST['remarks']  # Assuming the feedback field is the textarea with the id 'remarks'

        data = contactus(firstname=firstname, lastname=lastname, email=email, book_id=book_id, feedback=feedback)
        data.save()

        subject = 'Thank you for contacting Library Management System'
        message = f'Thank you for your feedback, {firstname} {lastname}! We appreciate your input.'
        from_email = '2200010045cseh@gmail.com'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return HttpResponse("<h1>Thank you for your feedback. An email has been sent to your provided address.</h1>")
    else:
        return HttpResponse("<h1>Error</h1>")

    #     send_mail(
    #         ' thank you contacting Library Management System',
    #         tosend,
    #         '2200010045cseh@gmail.com',
    #         [email],
    #         fail_silently=False,
    #     )
    #     return HttpResponse("<h1><center>Mail sent</center></h1>")
    # else:
    #     HttpResponse("<h1>error</h1>")
    #     # return redirect('newhomepage')
    #     # return render(request,'contact.html')
    #
    #     return HttpResponse("Sucess")

def feedback1(request):
    # You can keep the 'feedback' view as is or update it according to your requirements
    return render(request, 'librarianpatrols/thankyou.html')
