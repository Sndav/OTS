from django.views import View
from django.shortcuts import render, HttpResponseRedirect
from links.models import *



class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            link = Link.objects.get(user=request.user.id)
            return render(request, 'index.html', {
                'link': link
            })
        return render(request, 'index.html')

class RedirectView(View):
    def get(self, request):
        return HttpResponseRedirect(request.GET['url'])
