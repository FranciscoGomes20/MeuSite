from django.shortcuts import render
from .models import Menssagens
from .forms import MenssagensForm
from django.shortcuts import redirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MenssagensForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MenssagensForm()
    return render(request, 'index.html', {'form': form})
