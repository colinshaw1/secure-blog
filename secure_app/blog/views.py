from django.shortcuts import render

# Create your views here.
# create home page view
def home(request):
    return render(request, 'homepage.html', {})