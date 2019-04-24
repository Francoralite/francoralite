def handler404(request):
    return render(request, '404.html', status=404)
