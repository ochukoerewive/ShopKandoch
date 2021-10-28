from django.shortcuts import render

# Create your views here.
def become_vendor(request):
    return render(request, 'products/become_vendor.html')