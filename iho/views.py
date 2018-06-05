from django.shortcuts import render, redirect, render_to_response
from .models import Book, Author, BookInstance, Genre
from django.conf import settings
import os

from django.http import HttpResponse


def landing(request):
    return render(
        request,
        'landing.html'
    )


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={"home_active": "active",'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )


def about(request):
    return render(
        request,
        'about.html',
        context={"about_active": "active"}
    )


def gallery(request):
    path="C:\dev\store\media\iho"
    img_list = os.listdir(path)
    return render_to_response('gallery.html', {'images': img_list}, {"gallery_active": "active"})


def contact(request):
    return render(
        request,
        'contact.html',
        context={"about_active":"active"}
    )


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'simple_upload.html')

from iho.forms import ImageUploadForm


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageUploadForm()
    return render(
        request,
        'simple_upload.html',
        context={'form': form, "manage_active": "active"}
    )

