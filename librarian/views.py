from django.shortcuts import render , get_object_or_404, redirect
from .models import *
#from ..librarypatrons.models import BookApplicants


# Create your views here.
#manage books , users and borrowing activities
def managebooks(request):
    return render(request,'librarian/managebooks.html')

def add_book_details(request):
    if request.method == 'POST':
        BookTitle = request.POST.get('BookTitle')
        BookId = request.POST.get('BookId')
        BookYear = request.POST.get('BookYear')
        published_year = request.POST.get('published_year')
        remarks = request.POST.get('remarks')


        book_details = BookDetails(
            BookTitle=BookTitle,
            BookId=BookId,
            BookYear=BookYear,
            published_year=published_year,
            remarks=remarks

        )

        book_details.save()
        return render(request,'librarian/datainserted.html')
    return render(request,'librarianhomepage.html')

def view_book_details(request):
    book_details_list = BookDetails.objects.all()
    return render(request,'librarian/view_book_details.html',{'book_details_list':book_details_list})

def edit_book_details(request,book_id):
    book_details = get_object_or_404(BookDetails, id=book_id)
    if request.method == 'POST':
        book_details.BookTitle = request.POST.get('BookTitle')
        book_details.BookId = request.POST.get('BookId')
        book_details.BookYear = request.POST.get('BookYear')
        book_details.published_year = request.POST.get('published_year')
        book_details.remarks = request.POST.get('remarks')
        book_details.save()
        return redirect('librarian:view_book_details')
    else:
        return render(request,'librarian/edit_book_details.html',{'book_details':book_details})


def delete_book_details(request,book_id):
    book_details = get_object_or_404(BookDetails,id=book_id)
    if request.method=='POST':
        book_details.delete()
        return redirect('librarian:view_book_details')
    else:
        return render(request,'librarian/delete_book_details.html',{'book_details':book_details})


from librarypatrons.models import BookApplicants
def book_application_list(request):
    book_applications=BookApplicants.objects.all()
    return render(request,'librarian/book_application_list.html', {'book_applications':book_applications})

