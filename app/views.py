from django.views.generic import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', {
        })
class DetailView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/detail.html', {
        })
