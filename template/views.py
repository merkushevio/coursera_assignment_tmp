from django.shortcuts import render


# Create your views here.

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


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
