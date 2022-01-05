from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestUsefulness(EnumsTest):
    entity = 'usefulness'
    title = _("Fonction")
    data = [
        {"id":"1", "name":"danser", "notes":"Notes danser"}
    ]
    new_data = {"name":"jeu", "notes":"Notes jeu"}
