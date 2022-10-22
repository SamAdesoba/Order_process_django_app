from django.http import HttpResponse
from django.shortcuts import render

from order_process_app.templates import order_process_app_html


# Create your views here.
def home_view(request):
    return render(request, 'order_process_app_html/home.html')
