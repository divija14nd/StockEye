from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Verdict
from basicFunction import priceGraph 

from django.core.paginator import Paginator

# -------------------------------- Home function View -------------------------------- #
def home(request):
    qs = Verdict.objects.filter(verdict = "Strongly Recommend")
    paginator = Paginator(qs, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "data" : page_obj
    }
    return render(request, 'home_demo1.html', context)
# ----------------------------- Search Stock function View ----------------------------- #
def search_stock(request):
    stock_name = request.GET['stock_name']
    print(stock_name)
    graph = priceGraph(stock_name)
    return render(request,'stock_graph.html', {'graph': graph} )
# ----------------------------- Stock Detail function View ----------------------------- #
def detail(request):
    
    qs_strongly_recommended = Verdict.objects.filter(verdict = "Strongly Recommend")
    qs_recommended = Verdict.objects.filter(verdict = "Recomended")
    qs_not_recommended = Verdict.objects.filter(verdict = "Not Recomended")
    
    context = {
        "qs_strongly_recommended" : qs_strongly_recommended,
        "qs_recommended" : qs_recommended,
        "qs_not_recommended" : qs_not_recommended
    }
    
    return render(request, "detail.html", context)