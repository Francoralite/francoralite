from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestDomainVocal(EnumsTest):
    entity = 'emit_vox'
    title = _("Nature des émissions vocales")
    data = [
        {"id":"1", "name":"musique", "notes":"Musique avec un instrument"},
        {"id":"2", "name":"chanté", "notes":""}
    ]
    new_data = {"name":"parlé", "notes":"Notes parlé"}
