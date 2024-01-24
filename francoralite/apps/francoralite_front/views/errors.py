from django.shortcuts import render
from django.utils.translation import gettext as _

from ..tools import UserMessageHttp404


def csrf_failure(request, exception=None):
    return render(request, 'error.html', {
        'title': _('Accès non autorisé'),
        'message': _('Jeton CSRF invalide ! Veuillez ré-ressayer.'),
    }, status=403)


def handler400(request, exception=None):
    return render(request, 'error.html', {
        'title': _('Mauvaise requête'),
    }, status=400)


def handler403(request, exception=None):
    return render(request, 'error.html', {
        'title': _('Accès interdit'),
        'message': _('Vous n’avez pas l’autorisation d’accéder à cette page.'),
    }, status=403)


def handler404(request, exception=None):
    message = exception.args[0] if isinstance(exception, UserMessageHttp404) else None
    if not message:
        message = _('Nous sommes désolés, mais la page demandée est introuvable.')
    return render(request, 'error.html', {
        'title': _('Page introuvable'),
        'message': message,
    }, status=404)


def handler500(request, exception=None):
    return render(request, 'error.html', {
        'title': _('Erreur interne du serveur'),
        'message': _('Merci d’attendre quelques instants avant de ré-essayer ou de contacter votre administrateur si le problème persiste.'),
    }, status=500)
