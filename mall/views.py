from django.shortcuts import render, get_object_or_404
from django.views import View, generic

# Create your views here.


class IndexView (View):
    template_name = 'mall/index.html'