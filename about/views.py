from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class AboutView(View):
    template_name = 'about/index.html'

    def get(self, request):
        return render(request, self.template_name)