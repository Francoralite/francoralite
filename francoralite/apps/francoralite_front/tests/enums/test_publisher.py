from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestPublisher(EnumsTest):
    entity = 'publisher'
    title = _("Éditeur")
    data = [
        {"id":"1", "name":"editeur 1", "notes":"Notes éditeur 1"}
    ]
    new_data = {"name":"editeur 2", "notes":"Notes éditeur 2"}
