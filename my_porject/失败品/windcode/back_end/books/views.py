from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
# Create your views here.
from .models import Book,Chapter,Section
from django.core import serializers
import json

def book_list(requset):
    context = {}
    context['blogs'] = json.loads(serializers.serialize("json", Book.objects.all()))

    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})
    
def book_chapter(requset,slug):
    context = {}
    try:
        book_name = Book.objects.get(slug=slug)
        context['msg'] = 'success'
        context['books'] = json.loads(serializers.serialize("json", Chapter.objects.filter(book_name=book_name)))
    except Exception as e:
        context['msg'] = 'error'

    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})
