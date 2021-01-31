from django.views.generic import View
from django.shortcuts import render
from .models import Detail

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', {
        })
class DetailView(View):
    def get(self, request, *args, **kwargs):
        detail_data=Detail.objects.get(part="首")
        return render(request, 'app/detail.html', {
            "detail_data":detail_data
        })
