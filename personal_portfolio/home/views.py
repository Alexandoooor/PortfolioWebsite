from django.shortcuts import render
from home.models import BannerImage
# Create your views here.

def index(request):
    banner = BannerImage.objects.get(pk=2)
    context = {'banner': banner }
    return render(request, "home_index.html", context)
