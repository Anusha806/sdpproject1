from django.db import models

class BookDetails(models.Model):
    BookTitle = models.CharField(max_length=300)
    BookId = models.CharField(max_length=300)
    Book_Year = [
        ('1styear', '1st yr'),
        ('2ndyear', '2nd yr'),
    ]
    BookYear = models.CharField(max_length=20, choices=Book_Year)
    published_year = models.CharField(max_length=300)
    remarks = models.TextField()


    def __str__(self):
        return self.BookTitle

