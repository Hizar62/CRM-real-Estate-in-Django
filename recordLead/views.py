from django.shortcuts import render
from .forms import LeadRegistration

# Create your views here.
def add_Lead(request):
    if request.method == 'POST':
        fm = LeadRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = LeadRegistration()
    else:
        fm = LeadRegistration()

    return render(request,'recordLead/add.html', {'form':fm})

def show_Lead(request):
    return render(request, 'recordLead/show.html')

def update_Lead(request):
    return render(request, 'recordLead/update.html')