from django.shortcuts import render

def handler404(request, **kwargs):
    return render(request, '404.html', kwargs, status=404)
