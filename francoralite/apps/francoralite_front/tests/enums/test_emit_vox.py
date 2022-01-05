from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestDomainVocal(EnumsTest):
    entity = 'emit_vox'
    title = _("Nature des émissions vocales")
    data = [
        {"id":"1", "name":"musique", "notes":"Musique avec un instrument"}
    ]
    new_data = {"name":"chanté", "notes":"Notes chanté"}
