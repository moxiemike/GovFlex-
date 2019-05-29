from django.shortcuts import render
from .PullFBO import PullFBOdata

# Create your views here.
def search_view(request, *args, **kwargs):
  NAICScode = request.POST.get('title', '')
  PullFBOdata()
  
  return render(request, 'search.html', {})