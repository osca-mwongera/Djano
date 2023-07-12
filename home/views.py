import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(
        request=request, template_name='home/index.html', context=None, content_type=None, status=200, using=None
    )


