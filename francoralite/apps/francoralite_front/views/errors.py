from django.shortcuts import render
from django.utils.translation import gettext as _


def handler403(request, exception=None):
    return render(request, 'error.html', {
        'exception': exception or _('Accès interdit.'),
    }, status=403)


def handler404(request, exception=None):
    return render(request, 'error.html', {
        'exception': exception or _('Cette fiche n’existe pas.'),
    }, status=404)


def handler500(request, exception=None):
    return render(request, 'error.html', {
        'exception': _('Erreur indéterminée'),
    }, status=500)
