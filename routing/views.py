from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import http


def simple_route(request):
    if request.method == 'POST' or request.method == 'PUT':
        return HttpResponse(status=405)
    return HttpResponse(status=200)


@http.require_GET
def slug_route(request, param):
    return HttpResponse(content_type=param, status=200)


@http.require_GET
def sum_route(request, x, y):
    return HttpResponse(content_type=(int(x) + int(y)), status=200)


@http.require_GET
def sum_get_method(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    return HttpResponse(content_type=a + b, status=200)


@http.require_POST
def sum_post_method(request):
    a = int(request.POST.get('a'))
    b = int(request.POST.get('b'))
    return HttpResponse(content_type=a + b, status=200)


def echo(request):
    params = []
    try:
        if request.method == 'GET':
            for param in request.GET:
                params.append((param, request.GET[param]))
        elif request.method == 'POST':
            for param in request.POST:
                params.append((param, request.POST[param]))
        header = request.META.get('HTTP_X-PRINT-STATEMENT')
        context = {'statement': header, 'params': params, 'method': request.method.lower()}
    except Exception:
        pass
    return render(request, 'echo.html', context)

# from django.http import HttpResponse
# from django.views.decorators.http import require_GET, require_POST
#
#
# @require_GET
# def simple_route(request):
#     return HttpResponse()
#
#
# def slug_route(request, slug):
#     return HttpResponse(slug)
#
#
# def sum_route(request, a, b):
#     try:
#         a = int(a)
#         b = int(b)
#     except (ValueError, TypeError):
#         return HttpResponse(status=400)
#
#     return HttpResponse(a + b)
#
#
# @require_GET
# def sum_get_method(request):
#     try:
#         a = int(request.GET.get('a'))
#         b = int(request.GET.get('b'))
#     except (ValueError, TypeError):
#         return HttpResponse(status=400)
#
#     return HttpResponse(a + b)
#
#
# @require_POST
# def sum_post_method(request):
#     try:
#         a = int(request.POST.get('a'))
#         b = int(request.POST.get('b'))
#     except (ValueError, TypeError):
#         return HttpResponse(status=400)
#
#     return HttpResponse(a + b)
