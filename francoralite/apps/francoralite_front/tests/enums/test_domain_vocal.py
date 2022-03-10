from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestDomainVocal(EnumsTest):
    entity = 'domain_vocal'
    title = _('Genre vocal')
    data = [
        {"id":"1", "name":"comptine", "notes":"Notes comptine"}
    ]
    new_data = {"name":"air d'opéra", "notes":"Notes air d'opéra"}