from django.shortcuts import render

# Create your views here.

from quotes.models import Author,Categories,Quote
import json
from django.http import HttpResponse
from django.utils import simplejson

def authors(request):
    author_data = Author.objects.all()

    data = []
    for author in author_data:
        data.append({
            'name'          : author.name,
            'discription'   : author.author_discription,
            'info_url'      : author.author_url,
            'image'         : str(author.author_image)
        })

    print data

    return  HttpResponse(simplejson.dumps(data), mimetype='application/json')

def catgories(request):
    cat_data = Categories.objects.all()

    data = []
    for cat in cat_data:
        data.append({
            'name'          : cat.name,
            'cay_id'        : cat.id
        })

    print data

    return  HttpResponse(simplejson.dumps(data), mimetype='application/json')

def catgories2(request):
    cat_data = Categories.objects.all()

    data = []
    for cat in cat_data:
        data.append({
            'name'          : cat.name,
            'cay_id'        : cat.id
        })

    print data

    return  HttpResponse(simplejson.dumps(data), mimetype='application/json')

def quotes(request):
    quote_data=''
    if request.GET.get('authorid'):
        quote_data = Quote.objects.filter(author__id=request.GET.get('authorid'))
    elif request.GET.get('catid'):
        quote_data = Quote.objects.filter(category__id=request.GET.get('catid'))
    else:
        quote_data = Quote.objects.all()

    data = []
    for quote in quote_data:
        data.append({
            'quote_id'          : quote.quote_id,
            'description'       : quote.quote_discription,
            'author'            : quote.author.name,
            'cat_id'            : quote.category.id
        })

    return  HttpResponse(simplejson.dumps(data), mimetype='application/json')
