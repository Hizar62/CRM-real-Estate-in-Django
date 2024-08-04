from django.shortcuts import render, HttpResponseRedirect
from .forms import LeadRegistration
from .models import Lead
from django.contrib.auth.decorators import login_required, user_passes_test
from account.forms import SignUpForm, LoginForm
from django.shortcuts import render
from .models import Lead
from django.db.models import Sum
from recordLead import models

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

@login_required
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
     
@login_required
@user_passes_test(lambda u: u.is_manager or u.is_admin)     
def dashboard(request):
    paid_leads = Lead.objects.filter(payment_status='paid')
    pending_leads = Lead.objects.filter(payment_status='pending')

    paid_amount = paid_leads.aggregate(total=Sum('property_price'))['total'] or 0
    pending_amount = pending_leads.aggregate(total=Sum('property_price'))['total'] or 0
    
    context = {
        'paid_amount': paid_amount,
        'pending_amount': pending_amount,
    }
    return render(request, 'recordLead/dashboard.html', context)


