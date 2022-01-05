from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestLegalRights(EnumsTest):
    entity = 'legal_rights'
    title = _("Droits légaux")
    data = [
        {"id":"1", "name":"domaine public", "notes":"domaine public"},
        {"id":"2", "name": "droit d'auteur", "notes": "droit d'auteur"}
    ]
    new_data = {"name":"creative commons", "notes":"Notes creative commons"}