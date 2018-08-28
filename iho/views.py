from django.shortcuts import render, redirect, render_to_response
from .models import Book, Author, BookInstance, Genre
from django.conf import settings
import os

from django.http import HttpResponse

def index(request):
    return render(
        request,
        'index.html',
        context={"home_active": "active"},
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

