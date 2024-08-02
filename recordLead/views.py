from django.shortcuts import render

# Create your views here.
def add_Lead(request):
    return render(request,'recordLead/add.html')

def show_Lead(request):
    return render(request, 'recordLead/show.html')

def update_Lead(request):
    return render(request, 'recordLead/update.html')