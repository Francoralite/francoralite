from django.test import override_settings
from django.utils.translation import gettext as _


def test_handler_403(francoralite_context):
    """
    A function that handles a 403 error, performing actions on the francoralite_context.
    """
    francoralite_context.open_url("/fond/edit/1")
    francoralite_context.verify_title(_("Accès interdit"))


def test_handler_404(francoralite_context):
    """
    Handle the 404 error by opening the URL '/toto' and verifying the title 'Page introuvable'.
    """
    francoralite_context.open_url('/toto')
    francoralite_context.verify_title(_('Page introuvable'))


@override_settings(ROOT_URLCONF="francoralite.apps.francoralite_front.tests.urls_test")
def test_view_error_500(francoralite_context):
    """
    Test the view error 500 with the provided francoralite context.
    """
    francoralite_context.open_url('/test-err500/')
    francoralite_context.verify_title(_("Erreur interne du serveur"))
