from django.shortcuts import render, HttpResponseRedirect
from .forms import LeadRegistration
from .models import Lead

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
        leads = Lead.objects.all()  # Query all leads
        return render(request, 'recordLead/show.html', {'leads': leads})

def update_Lead(request,id):
    if request.method == 'POST':
         pi = Lead.objects.get(pk=id)
         fm = LeadRegistration(request.POST, instance=pi)
         if fm.is_valid():
              fm.save()
    else:
        pi = Lead.objects.get(pk=id)
        fm = LeadRegistration(instance=pi)              
    return render(request, 'recordLead/update.html', {'form':fm})
    

def delete_Lead(request,id):
     if request.method == 'POST':
          pi = Lead.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/show')
     
def dashboard(request):
     return render(request, 'recordLead/dashboard.html')