from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    if request.method == "POST":
        poem_ins = Poems()
        poem_ins.poem = request.POST.get('poem')
        poem_ins.save()

        print("Poem saved")

    poems = Poems.objects.all()

    context = {
        "poem_count": len(poems)
    }

    return render(request, 'index.html', context=context)