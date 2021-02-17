from django.shortcuts import render
from .tasks import crawl_domain
from django.shortcuts import redirect
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def CrawlView(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data['url']
        crawl_domain(url)
        return redirect('/')

