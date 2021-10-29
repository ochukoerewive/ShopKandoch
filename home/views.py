from django.shortcuts import render

# Create your views here.

def index(request):
    """view to return the index page"""

    return render(request, 'home/index.html')

# contact page.
def contact(request):
    """view to return the contact page"""

    return render(request, 'home/contact.html')

def become_vendor(request):
    return render(request, 'vendor/become_vendor.html')
