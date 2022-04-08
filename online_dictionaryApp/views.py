from django.shortcuts import render
from .forms import DictionaryForm
from .models import DictionaryDB


def home(request):
    if request.method=="POST":
        form=DictionaryForm(request.POST or None)
        if form.is_valid():
            form.save()

            all_entry=DictionaryDB.objects.all().order_by('alphabet')
            return render(request, 'index.html',{'all_entry':all_entry})
    else:

        all_entry = DictionaryDB.objects.all().order_by('alphabet')
        return render(request, 'index.html', {'all_entry': all_entry})


def details(request, details_id):
    details=DictionaryDB.objects.get(id=details_id)
    return render(request, 'details.html', {'details':details})






