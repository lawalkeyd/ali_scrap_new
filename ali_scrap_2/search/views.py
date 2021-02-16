from django.shortcuts import render
from .tasks import crawl_domain
from django.shortcuts import redirect

# Create your views here.

def CrawlView(request):
    if request.method == 'POST':
        url = request.POST['url']
        crawl_domain(url)
        return redirect('/')

