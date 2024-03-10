from django.db import models

# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    Branch = [
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('AgBSC', 'AgBSC'),
    ]
    Branch = models.CharField(max_length=20, choices=Branch)
    Year = [
        ('1st yr', '1st yr'),
        ('1st yr', '2nd yr'),
        ('3rd yr', '3rd yr'),
        ('4th yr', '4th yr'),
    ]
    Year = models.CharField(max_length=20, choices=Year)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class contactus(models.Model):
    firstname=models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.TextField(primary_key=True)
    book_id = models.TextField(max_length=255)
    feedback = models.TextField(max_length=255)
    class Meta:
        db_table="contactus"

from librarian.models import BookDetails
class BookApplicants(models.Model):
    book_details = models.ForeignKey(BookDetails, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    id_document=models.FileField(upload_to='id_document/')
    department=models.TextField()
    def __str__(self):
        return f"{self.name} - {self.book_details}"

