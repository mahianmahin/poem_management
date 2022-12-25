import fnmatch
import os
from datetime import date

from django.core.files.base import ContentFile, File
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .models import *


def file_count():
    return len(fnmatch.filter(os.listdir("pdf/"), '*.*'))


def create_pdf(unsaved_poems):

    context = {
        "poems": unsaved_poems
    }

    template_path = 'pdf_template.html'
    response = HttpResponse(content_type='text/html')
    template = get_template(template_path)
    html = template.render(context)

    count = file_count()

    with open(f'pdf/poem_book_{count+1}.html', "w", encoding="utf-8") as file:
        file.write(html)
        file.close()

    return f"[+] poem_book_{count+1}.html created"



def index(request):
    poems = Poems.objects.all()

    if request.method == "POST":
        poem_ins = Poems()
        poem_ins.poem = request.POST.get('poem')
        poem_ins.save()

        print("Poem saved")

        unsaved_poems = Poems.objects.filter(added_to_book=False)
        
        if len(unsaved_poems) >= 50:
            pdf = create_pdf(unsaved_poems)
            print(pdf)

            for poem in unsaved_poems:
                poem.added_to_book = True
                poem.save()
    


    context = {
        "poem_count": len(poems),
        "book_count": file_count()
    }

    return render(request, 'index.html', context=context)


def pdf_template(request):
    poems = Poems.objects.all()

    context = {
        "poems": poems
    }

    return render(request, 'pdf_template.html', context=context)