from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden,HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import redirect, render

def index(request):
    return HttpResponse('<h1>Страница приложения</h1> ')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена 404</h1>')

def pageForbidden(request, exception):
    return HttpResponseForbidden('<h1> Permission Denied Sorry(</h1>')

def HttpResponseBadRequest(request, exception):
    return HttpResponseBadRequest("<h1> Bad Request Sorry(</h1>")

def HttpResponseServerError(request):
    return HttpResponseServerError("<h1>500 Internal Server Error</h1>")